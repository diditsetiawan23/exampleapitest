import requests
import json
import os
import re
from urllib3 import exceptions as urlexc
from requests import exceptions as reqexc
import datetime
from mergedeep import merge

class ApiTestWrapper:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.datenow = self.now.strftime("%d-%m-%Y")

    @staticmethod
    def request_type(type):
        allowed_methods = ["GET", "POST", "DELETE", "PUT"]
        if type in iter(allowed_methods):
            return type

    @staticmethod
    def init_json_report(feature_title):
        # store json file
        parent_key = feature_title
        parent_dict = {parent_key: None}
        cdict, ddict = {}, {}
        json_dict = [parent_dict, parent_key, cdict, ddict]
        return json_dict

    def send_request(self,type,api_path,headers,payload=None,json_payload=None,files=None,cookie=None):
        request_type = self.request_type(type=type)
        with requests.Session() as session:
            resp = session.request(
                method=request_type,
                url=api_path,
                headers=headers,
                data=payload,
                files=files,
                cookies=cookie,
                json=json_payload,
            )
            resp_time = str(resp.elapsed.total_seconds())
            print(f"Request to {api_path}")
            print(f"Getting response in {resp_time} second")
            return resp
        
    def pretty_print_request(self, request):
        print(
            "\n{}\n{}\n\n{}\n\n{}\n".format(
                "-----------Request----------->",
                request.method + " " + request.url,
                "\n".join("{}: {}".format(k, v) for k, v in request.headers.items()),
                request.body,
            )
        )

    def pretty_print_response(self, response: requests.Response):
        print(
            "\n{}\n{}\n\n{}\n\n{}\n".format(
                "<-----------Response-----------",
                "Status code:" + str(response.status_code),
                "\n".join("{}: {}".format(k, v) for k, v in response.headers.items()),
                response.text,
            )
        )

    def save_json_record(self, dict, platform_name):
        jsonpath = os.getcwd() + os.path.join(
            "/",
            "reports/json_reports/"
            + platform_name
            + "_json_reports_"
            + self.datenow
            + ".json",
        )
        filejson = jsonpath
        with open(filejson, "w") as fp:
            json.dump(dict, fp)

    def json_test_record(
        self,
        platform_name,
        parent_dict,
        parent_key,
        dict,
        ddict,
        feature_as_key,
        nested,
        exp_result,
        act_result,
        value,
        key=None,
    ):
        jsonpath = os.getcwd() + os.path.join(
            "/",
            "reports/json_reports/"
            + platform_name
            + "_json_reports_"
            + self.datenow
            + ".json",
        )
        dict.setdefault(feature_as_key, {})
        dict[f"{feature_as_key}"].setdefault(nested, {})
        if nested == "key_exits":
            nested_dict = dict[f"{feature_as_key}"][f"{nested}"].setdefault(key, {})
            nested_dict.setdefault("expected_result", exp_result)
            nested_dict.setdefault("actual_result", act_result)
            nested_dict.setdefault("result", value)
        else:
            dict[f"{feature_as_key}"][f"{nested}"].setdefault(
                "expected_result", exp_result
            )
            dict[f"{feature_as_key}"][f"{nested}"].setdefault(
                "actual_result", act_result
            )
            dict[f"{feature_as_key}"][f"{nested}"].setdefault("result", value)
        parent_dict[parent_key] = dict
        if parent_dict[parent_key] is not None:
            if dict not in list(parent_dict[parent_key]):
                parent_dict[parent_key] = dict
        platform = {platform_name: parent_dict}
        if os.path.isfile(jsonpath):
            with open(jsonpath, "r+") as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # merge dict object
                merge(file_data, platform)
                # Sets file's current position at offset.
                filejson = jsonpath
                with open(filejson, "w") as fp:
                    json.dump(file_data, fp, indent=4)
        else:
            self.save_json_record(platform, platform_name)
        return platform
    
    def api_response(self, response):
        api_response = response.text
        print(f"Response : {api_response}")
        return api_response
    
    def get_keys(self,json_data, prefix=""):
        keys = []
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                new_prefix = f'{prefix}["{key}"]' if prefix else f'"{key}"'
                keys.extend(self.get_keys(value, new_prefix))
        elif isinstance(json_data, list):
            for index, item in enumerate(json_data):
                new_prefix = f"{prefix}[{index}]"
                keys.extend(self.get_keys(item, new_prefix))
        else:
            if prefix:
                keys.append(prefix)
        return keys
    
    def compare_json_keys(self,json1, json2):
        keys1 = self.get_keys(json1)
        keys2 = self.get_keys(json2)
        missing_keys = list(set(keys1) - set(keys2))
        return set(keys1) == set(keys2), missing_keys
    
    def not_found_key(self,platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,key):
        print("Key doesn't exist in JSON data")
        logtxt = f"Expected Key : {key} Not Found"
        print(logtxt)
        value = "N/A"
        result = False
        print(f"Key Exist : {str(result)}")
        print(f"Key Value : {value}")
        self.json_test_record(
            platform_name,
            parent_dict,
            parent_key,
            child_dict,
            d_dict,
            test_case,
            f"key_exits",
            f"{key}",
            logtxt,
            result,
            key,
        )
        return result

    def found_key(self,key,platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload
    ):
        print("Key exist in Response data")
        pattern = r'^\["\w+"\]\[\d+\]\["\w+"\]$'
        if re.match(pattern, key):
            value = eval("json_payload" + key)
        elif key == "All Expected Key":
            value = "All Key Are Exist"
        elif isinstance(json_payload, list):
            value = str(json_payload[0][key])
        else:
            value = str(json_payload[key])
        logtxt = f"Expected Key : {key} Found"
        print(logtxt)
        result = True
        print(f"Key Exist : {str(result)}")
        print(f"Key Value : {value}")
        self.json_test_record(
            platform_name,
            parent_dict,
            parent_key,
            child_dict,
            d_dict,
            test_case,
            f"key_exits",
            f"{key}",
            logtxt,
            result,
            key,
        )
        return result

    def validate_status_code(self,platform_name,expected_status_code,response,parent_dict,parent_key,child_dict,d_dict,test_case,):
        status_code = response.status_code
        print(f"Status Code : {str(status_code)}")
        if expected_status_code == status_code:
            result = True
            print(f"Response Status Code : {str(status_code)}, Expected Status Code : {str(expected_status_code)}")
        else:
            print(f"Response Status Code : {str(status_code)}, Expected Status Code : {str(expected_status_code)}")
            result = False
        return self.json_test_record(
            platform_name,
            parent_dict,
            parent_key,
            child_dict,
            d_dict,
            test_case,
            "status_code",
            str(expected_status_code),
            str(status_code),
            result,
        )
    
    def validate_json(self,platform_name,response,parent_dict,parent_key,child_dict,d_dict,test_case
    ):
        json_data = response.text
        try:
            json.loads(json_data)
            print("JSON Valid : True")
            print(f"Response JSON Check : {str(True)}, Expected JSON Check : {str(True)}")
            result = True
        except ValueError as err:
            print("JSON Valid : False")
            print(
                f"Response JSON Check : {str(False)}, Expected JSON Check : {str(True)}")
            result = False
        return self.json_test_record(
            platform_name,
            parent_dict,
            parent_key,
            child_dict,
            d_dict,
            test_case,
            "json_valid",
            str(True),
            result,
            result,
        )
    
    def check_key_in_json(self,platform_name,key,response,parent_dict,parent_key,child_dict,d_dict,test_case):
        json_data = response.text
        pattern = r'^\["\w+"\]\[\d+\]\["\w+"\]$'
        try:
            json_payload = json.loads(json_data)
            try:
                if json.loads(key):
                    expected_json = json.loads(key)
                    compare_result, missing_keys = self.compare_json_keys(expected_json, json_payload)
                    if compare_result:
                        result = self.found_key("All Expected Key",platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload)
                    else:
                        if len(missing_keys) == 0:
                            result = self.found_key("All Expected Key",platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload)
                        else:
                            for i in missing_keys:
                                result = self.not_found_key(platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,i)
            except (json.JSONDecodeError, TypeError):
                print("Expected key value are not in JSON format, changed to different approach")
                if not isinstance(key, list):
                    list_of_key = key.split(",")
                    key = list_of_key
                for i in key:
                    if re.match(pattern, i):
                        try:
                            if eval("json_payload" + i):
                                result = self.found_key(i,platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload)
                            else:
                                result = self.not_found_key(platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,i)
                        except KeyError:
                            result = self.not_found_key(platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,i)
                    elif isinstance(json_payload, list):
                        if i in json_payload[0]:
                            result = self.found_key(i,platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload)
                        else:
                            result = self.not_found_key(platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,i)
                    else:
                        if i in json_payload:
                            result = self.found_key(i,platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,json_payload)
                        else:
                            result = self.not_found_key(platform_name,parent_dict,parent_key,child_dict,d_dict,test_case,i)
        except ValueError as err:
            result = False
        return result
    
    def validate_response_time(self,platform_name,resp_limit,response,parent_dict,parent_key,child_dict,d_dict,testcase):
        resp_time = response.elapsed.total_seconds() * 1000
        resp_ms = round(resp_time)
        print(f"Getting response in {str(resp_ms)} ms")
        if resp_ms <= resp_limit:
            result = True
            print(f"Actual Response Time : {str(resp_ms)}ms, Expected Response Time : {str(resp_limit)}ms")
        else:
            print(f"Actual Response Time : {str(resp_ms)}ms, Expected Response Time : {str(resp_limit)}ms")
            result = False

        return self.json_test_record(
            platform_name,
            parent_dict,
            parent_key,
            child_dict,
            d_dict,
            testcase,
            "response_time",
            f"{str(resp_limit)}ms",
            f"{str(resp_ms)}ms",
            result,
        )
    
    def api_check(self,method,api_endpoint,header,payload,cookie,platform,expected_status_code,api_test_title,example_response,expected_response_time,dict,json_check=None,):
        try:
            response = self.send_request(
                method, api_endpoint, header, json_payload=payload, cookie=cookie
            )
            self.pretty_print_request(response.request)
            self.validate_status_code(platform,expected_status_code,response,dict[0],dict[1],dict[2],dict[3],api_test_title,)
            self.api_response(response)
            if not json_check:
                print("Response Format Not Checked")
            elif json_check:
                self.validate_json(platform,response,*dict[:4],api_test_title,)
            if example_response != "":
                self.check_key_in_json(platform,example_response,response,*dict[:4],api_test_title,)
            self.validate_response_time(platform,expected_response_time,response,*dict[:4],api_test_title)
            self.pretty_print_response(response)
            return response
        except (urlexc.NewConnectionError,urlexc.MaxRetryError,reqexc.ConnectionError) as e:
            print("Connection Error, Please check the Endpoint !!!")
            print(e)

    def execute_api_test(self,test_title,method,data,header,cookie,platform,status_code,response_time,dict,json_check=None,):
        print(data.get("api"))
        saved_key = test_title.lower().replace(" ", "_")
        response = self.api_check(method,data.get("api"),header,data.get("payload"),cookie,platform,status_code,saved_key,data.get("response"),response_time,dict,json_check  )
        return response
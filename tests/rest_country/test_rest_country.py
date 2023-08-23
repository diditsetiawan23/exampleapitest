import unittest
import concurrent.futures
from function import wrap
from config import global_config as config
from data.middle.rest_country import data_rest_country as data

#calling wrapper
wrapper = wrap.ApiTestWrapper()


# initiate json record
json_dict = wrapper.init_json_report("rest_country")

class TestRestCountry(unittest.TestCase):

    def test_001_get_country_by_valid_name(self):
        wrapper.execute_api_test(
            "get_country_by_valid_name"
            ,"GET"
            ,data.get_country_by_valid_name
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_002_get_country_by_invalid_name(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_name"
            ,"GET"
            ,data.get_country_by_invalid_name
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_003_get_country_by_valid_full_name(self):
        wrapper.execute_api_test(
            "get_country_by_valid_full_name"
            ,"GET"
            ,data.get_country_by_valid_full_name
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )
    
    def test_004_get_country_by_invalid_full_name(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_full_name"
            ,"GET"
            ,data.get_country_by_invalid_full_name
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_005_get_country_by_valid_code(self):
        wrapper.execute_api_test(
            "get_country_by_valid_code"
            ,"GET"
            ,data.get_country_by_valid_code
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_006_get_country_by_invalid_code(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_code"
            ,"GET"
            ,data.get_country_by_invalid_code
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_007_get_country_by_valid_list_code(self):
        wrapper.execute_api_test(
            "get_country_by_valid_list_code"
            ,"GET"
            ,data.get_country_by_valid_list_code
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_008_get_country_by_invalid_list_code(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_list_code"
            ,"GET"
            ,data.get_country_by_invalid_list_code
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_009_get_country_by_valid_currency(self):
        wrapper.execute_api_test(
            "get_country_by_valid_currency"
            ,"GET"
            ,data.get_country_by_valid_currency
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_010_get_country_by_invalid_currency(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_currency"
            ,"GET"
            ,data.get_country_by_invalid_currency
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_011_get_country_by_valid_demonym(self):
        wrapper.execute_api_test(
            "get_country_by_valid_demonym"
            ,"GET"
            ,data.get_country_by_valid_demonym
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_012_get_country_by_invalid_demonym(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_demonym"
            ,"GET"
            ,data.get_country_by_invalid_demonym
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

    def test_013_get_country_by_valid_language(self):
        wrapper.execute_api_test(
            "get_country_by_valid_language"
            ,"GET"
            ,data.get_country_by_valid_language
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )
    
    def test_014_get_country_by_invalid_language(self):
        wrapper.execute_api_test(
            "get_country_by_invalid_language"
            ,"GET"
            ,data.get_country_by_invalid_language
            ,None
            ,None
            ,"example_api_test"
            ,200
            ,1000
            ,json_dict
            ,True
        )

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(unittest.main())
    
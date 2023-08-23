from data.api.rest_country import api_rest_country as api
from data.response.rest_country import response_rest_country as response

get_country_by_valid_name = {
    "api": f"{api.get_country_by_name}indo",
    "payload":None,
    "response":response.get_country_by_name,
}

get_country_by_invalid_name  = {
    "api": f"{api.get_country_by_name}jcbebwjwk",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_full_name = {
    "api": f"{api.get_country_by_name}indonesia{api.param_for_full_name}",
    "payload":None,
    "response":response.get_country_by_full_name,
}

get_country_by_invalid_full_name = {
    "api": f"{api.get_country_by_name}hsvdhwvwjh{api.param_for_full_name}",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_code = {
    "api": f"{api.get_country_by_code}id",
    "payload":None,
    "response":response.get_country_by_code,
}

get_country_by_invalid_code = {
    "api": f"{api.get_country_by_code}6sgys",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_list_code = {
    "api": f"{api.get_country_by_list_code}id,my",
    "payload":None,
    "response":response.get_country_by_list_code,
}

get_country_by_invalid_list_code = {
    "api": f"{api.get_country_by_list_code}6gy,jbw7w",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_currency = {
    "api": f"{api.get_country_by_currency}rupiah",
    "payload":None,
    "response":response.get_country_by_currency,
}

get_country_by_invalid_currency = {
    "api": f"{api.get_country_by_currency}kfwuw8",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_demonym = {
    "api": f"{api.get_country_by_demonym}indonesian",
    "payload":None,
    "response":response.get_country_by_demonym,
}

get_country_by_invalid_demonym = {
    "api": f"{api.get_country_by_demonym}indosiar",
    "payload":None,
    "response":response.country_not_found,
}

get_country_by_valid_language = {
    "api": f"{api.get_country_by_language}bahasa",
    "payload":None,
    "response":response.get_country_by_language,
}

get_country_by_invalid_language = {
    "api": f"{api.get_country_by_language}yhsvwuywj",
    "payload":None,
    "response":response.country_not_found,
}
from config import global_config

base_url = global_config.url_config.get("REST-COUNTRY")
get_country_by_name = f"{base_url}v3.1/name/"
param_for_full_name = '?fullText=true'
get_country_by_code = f"{base_url}v3.1/alpha/"
get_country_by_list_code = f"{base_url}alpha?codes="
get_country_by_currency = f"{base_url}v3.1/currency/"
get_country_by_demonym = f"{base_url}v3.1/demonym/"
get_country_by_language = f"{base_url}v3.1/lang/"
import requests
from urllib.parse import urlparse
import time
def show_scanner(target_address):
    http_response = {}
    http_status_code = {}
    protocol = {}
    header_list = ["Server", "Content-Type", "Content-Length"]
    try:

        check_url = urlparse(target_address)
        protocol["protocol"] = check_url.scheme
        start_time = time.time()
        request_validate = requests.get(target_address, timeout=5)
        http_status_code["Status Code"] = request_validate.status_code
        end_time = time.time()
        response_time = end_time - start_time
        for header in header_list:
            response_check = request_validate.headers[header]
            http_response[header] = response_check 
        
    except:
        print(f"Network or server error occurred:")    
    return http_response, http_status_code, protocol, header_list, response_time


    
def show_parser(response, protocol):

    http_response = {}
    https_response = {}
    header_list = ("Server", "Content-Type", "Content-Lemgth")
    try: 
     if protocol == 'http://':
        for header in header_list: 
         http_response[header] = response.headers.get(header, "")
     elif protocol == 'https://':
        for https_header in header_list:
           https_response[https_header] = response.headers.get(https_header, "")
     response.close()    
    except response.exceptions.RequestException as e:
        print(f"Network or server error occurred: {e}")  
    return http_response, https_response, header_list        
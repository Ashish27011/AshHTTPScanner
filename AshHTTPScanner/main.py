from banners import banner
from core import validator
from core import scanner
from core import reporter
from outputs import writeup

target_address = validator.show_validator()
print("")
banner.s_banner()
print("")
http_response, http_status_code, protocol, header_list, response_time = scanner.show_scanner(target_address)
reporter.show_report(target_address, http_response, http_status_code, protocol, header_list, response_time) 
writeup.show_writeup(target_address, http_response, http_status_code, protocol, header_list, response_time) 
print("")
banner.e_banner()
from urllib.parse import urlparse
def show_validator():
    while True:
        try: 
            target_address = input("Enter Target : ")
            validate_input = urlparse(target_address)
            if validate_input.scheme not in ['http', 'https']:
                print("Invalid scheme! Use http or https")
                continue
            elif not validate_input.netloc:
                print("Invalid URL! Missing domain")
                continue
            else:
                break
        except:
            print("Enter Valid URL!")
            continue    
    return target_address

#!/usr/bin/env python3
import platform
import ipaddress
import socket
import tls_check
import client
import validators
import re
import client_tls

def main():

    global port
    global host
    
    response = input("Enter an IP or hostname address: ")
    print(response)
    
    
    try:
        if re.match("^\w+$", response):
            host = response
            
    
        elif validators.domain(response):
            host = response
            
        else:
            ip = ipaddress.ip_address(response)
#            print(ip)
            host = response
    except:
        print("Oopsie woopsie, we did a fuckywucky")
        exit()
        
    finally:
        response = input("Enter a port: ")       
        

    try:
        response = int(response)
        if response <= 65535 and response >= 0:
            port = response
            print(port)
        else:
            print("Port is invalid: " + \
            str(response))
            exit()
    except ValueError:
        print("Port is not a valid value: " + \
        str(response))
        exit()
    except:
        print("Oopsie woopsie, we did a fuckywucky")
        exit()
        
    finally:
        tls_check.checktls(host,port)

        
        
if __name__ == "__main__":
    main()

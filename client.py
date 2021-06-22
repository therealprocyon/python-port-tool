#!/usr/bin/env python3
import socket
import string

def start_conn(host,port):


    addr = (host,port)
        
    
    response = input("Enter buffer size: ")
    try:
       response = int(response)
       if response <= 65535 and response >= 0:
           BUFFER_SIZE = response
           print(BUFFER_SIZE)
       else:
            print("The buffersize is invalid: " + \
            str(response))
            exit()
    except ValueError:
        print("The input is invalid: " + \
        response)
        exit()
    except:
        print("Oopsie woopsie, we did a fuckywucky")
        exit()
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(addr)
        request = input("Enter your request header: ")
        byte_request = request.encode('utf-8')
        s.sendall(b"" + byte_request)
        while True:
            data = s.recv(BUFFER_SIZE)
            data = str(data, 'utf-8')
            if ( len(data) < 1 ):
                break
            print(data)
   
   

#!/usr/bin/env python3
import socket
import string
import sys

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
        
    print("Enter your request header: ")
    request = sys.stdin.buffer.readline()
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(addr)
        s.send(request)
        while True:
            data = s.recv(BUFFER_SIZE)
            if ( len(data) < 1 ):
                break
            sys.stdout.buffer.write(data)
   

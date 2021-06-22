#!/usr/bin/env python3
import socket
import ssl
import string
import pprint


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
    
    request = input("Enter your request header: ")
    context = ssl.create_default_context() 



    with socket.create_connection(addr) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            while True:
                try:
                    ssock.do_handshake()
                    break
                except ssl.SSLWantReadError:
                    select.select([sock], [], [])
                except ssl.SSLWantWriteError:
                    select.select([], [sock], [])
            cert = ssock.getpeercert()
            pprint.pprint(cert)
            print(ssock.version())
            ssock.sendall(request.encode())
            while True:
                data = ssock.recv(BUFFER_SIZE)
                print(data)
                if ( len(data) < 1 ):
                    break

   
   

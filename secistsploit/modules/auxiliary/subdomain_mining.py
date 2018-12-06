# -*- coding: UTF-8 -*-
import re
from bs4 import BeautifulSoup
from secistsploit.core.exploit import *
from secistsploit.core.http.http_client import HTTPClient

class Exploit(HTTPClient):
    __info__ = {
        "name": "subdomain_mining",
        "description": "subdomain_mining",
        "authors": (
            "jjiushi",
        ),
        "references": (
            "www.422926799.github.io"
            "www.422926799.github.io"
        ),

    }

    target = OptString("i.links.cn", "Query through this website")
    port = OptPort(80, "Target HTTP port")
    rdomain = OptString("","Target Domain")
    def __init__(self):
        self.endianness = "<"

    def run(self):
        domain=(self.target)
        rdoa=(self.rdomain)
        data = {
            'b2':1,
            'b3':1,
            'b4':1,
            'domain':'{}'.format(rdoa),
        }
        response = self.http_request(
            method="POST",
            path="/subdomain/",
            data=data,
        )
        print('[+] Query result')
        zz=re.findall('<a href=".*" rel=nofollow target=_blank>.*</a>',str(response.text))
        for z in zz:
            dr=BeautifulSoup(str(z),'html.parser')
            print(dr.get_text())
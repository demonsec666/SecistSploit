# -*- coding: UTF-8 -*-
import os
from secistsploit.core.exploit import *
from secistsploit.core.http.http_client import HTTPClient

class Exploit(HTTPClient):
    __info__ = {
        "name": "scanning_directory",
        "description": "scanning_directory",
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
    def __init__(self):
        self.endianness = "<"

    def run(self):
        rhost=(self.target)
        port=(self.port)
        oklist=[]
        blackhit=['404','Not Found','护卫神','360','安全狗','无权访问','403','Hacking','D盾','不存在']
        print('[+] RHOST IP:{}'.format(rhost))
        print('[+] RPORT PORT:{}'.format(port))
        while True:
            ljzd = input('Dictionary path:')
            if os.path.exists(ljzd):
                print('[+] {} ok'.format(ljzd))
                break
            else:
                print('[-] {} not found'.format(ljzd))
                continue
        dk=open('{}'.format(ljzd),'r')
        for r in dk.readlines():
            sc="".join(r.split('\n'))
            response = self.http_request(
                method="GET",
                path="{}".format(sc)
            )
            for b in blackhit:
                if response is not None and response.status_code==200 and not b in response.text:
                    ok='[+] Path:{} | statuscode:{}'.format(response.url,response.status_code)
                    if ok in oklist:continue
                    oklist.append(ok)

        if len(oklist)>0:
            for k in oklist:
                print(k)
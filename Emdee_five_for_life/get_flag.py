#!/usr/bin/env python3

import requests
import hashlib

url = "http://206.189.121.131:32150/"

with requests.Session() as r:
    data = r.get(url)
    data = data.text
#    print(data)

    end = '</h3><center>'

    find = data.index(end)
    string= data[find - 20:187]
    print(f'String: {string}')

    hashed = hashlib.md5(string.encode()).hexdigest()

    print(f'MD5 SUM: {hashed}')


    payload = {'hash':hashed}

    post = r.post(url, data=payload)

    flag = post.text
    print(flag)

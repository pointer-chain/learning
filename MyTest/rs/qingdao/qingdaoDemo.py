import json
import urllib

import requests
import re
import execjs
import subprocess

from py_mini_racer import MiniRacer

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


url = 'http://qingdao.chinatax.gov.cn/search/was5/web/search?channelid=223090&dqe%3c%3edata()'
res = requests.get(url, headers=headers, timeout=3, verify=False)
print(res)
print(res.text)
cookie = res.cookies.get_dict()
for key in cookie.keys():
    if key.endswith("S"):
        cookie_name_1 = key
        cookie_name_2 = key[0: -1] + "T"
    elif key.endswith("O"):
        cookie_name_1 = key
        cookie_name_2 = key[0: -1] + "P"

if res.status_code in [412, 202, 200]:
    nsd = re.findall(r'_ts\.nsd=(\d+?);', res.text, re.S)[0]
    cd = re.findall(r'_ts\.cd=(.+?);', res.text, re.S)[0][1:-1]
    params = {
        'nsd': nsd,
        'cd': cd,
        'user_agent': headers['user-agent'],
    }
    with open('js/rs_qingdao_etax.js', 'r', encoding='utf-8') as fr:
        fr_cont = fr.read()

    vm_ctx = MiniRacer()
    vm_ctx.eval(fr_cont)
    cookie_p = vm_ctx.call('get_cookie', params)
    cookie[cookie_name_2] = "0" + cookie_p['cookie']

    print(cookie)
    print(url)
    res = requests.get(url, headers=headers, cookies=cookie, verify=False, allow_redirects=False)
    print(res.status_code)
    print(res.text)
    print(res.cookies.get_dict())
    print(res.url)
    print(res.cookies.keys())
    print(res.headers)
from http.server import BaseHTTPRequestHandler
import json
from bs4 import BeautifulSoup
import requests
def login(a,b):
    data={
'token':"",
'username':a,
'password':b,
'rememberme':"on"
    }
    session=requests.session()
    post=session.post('https://my.freenom.com/dologin.php',data=data,allow_redirects=False)
    cookies = requests.utils.dict_from_cookiejar(session.cookies) 
    return cookies
def freenom_renew(a,b):
    cookies=login(a,b)
    headers={
  "Host": "my.freenom.com",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:103.0) Gecko/20100101 Firefox/103.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Accept-Encoding": "gzip, deflate, br",
  "Referer": "https://my.freenom.com/domains.php?a=renewals",
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "TE": "trailers"
}
    url='https://my.freenom.com/domains.php?a=renewals'
    get=requests.get(url,headers=headers,cookies=cookies)
    text=get.text
    #print(text)
    bf=BeautifulSoup(text,'html.parser')
    tbody=bf.find_all('tr')
    text=''
    for td in tbody:
        td=td.find_all('td')
        for td in td:
            td=str(td)
            text=text+'<br>'+td
	 #print(a.find_all('a'))
    text=text.replace('Advance Renewal is 14 Days for Free Domains','')
    text=text.replace('domains.php','https://my.freenom.com/domains.php')
    text=text.replace('amp;','')
    print('完成')
    return text
#print(freenom_renew("3408006879@qq.com","Qw1357924680"))
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        ip=self.client_address[0]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        text=freenom_renew("3408006879@qq.com","Qw1357924680")
        data={'code':200,'msg':'成功','ip':ip,'text':text}
        res=json.dumps(data)
        self.wfile.write(res.encode())
        return
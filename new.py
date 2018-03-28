import urllib.request
import ssl
import base64
import requests
import json

def convert_image():
    # Picture ==> base64 encode
    with open('TB1._pmLXXXXXb6apXXunYpLFXX.jpg', 'rb') as fin:
        image_data = fin.read()
        base64_data = base64.b64encode(image_data)
    return base64_data
with open('demo.txt','w') as f:
    f.write(str(convert_image()))

host = 'https://ocrapi-ecommerce.taobao.com'
path = '/ocrservice/ecommerce'
method = 'POST'
appcode = ''
querys = ''
bodys = {}
url = host + path
bodys['img'] = convert_image().decode()
post_data = bodys['img']

print(post_data)
# request = urllib.request.Request(url, post_data)
# request.add_header('Authorization', 'APPCODE ' + appcode)
payload = {'img':post_data }
headers = {'Authorization': 'APPCODE ' + appcode}
r = requests.post(url,data=json.dumps(bodys),headers=headers)
print('response:',r)
print('X-Ca-Request-Id:',r.headers['X-Ca-Request-Id'])
print(r.text)
print(r.content)
r.json()
print(r.json())
result = []
for i in r.json()['prism_wordsInfo']:
    pos = []
    for j in i['pos']:
        pos.append(j['x'])
        pos.append(j['y'])
    pos.append(i['word'])
    result.append(pos)
print(result)
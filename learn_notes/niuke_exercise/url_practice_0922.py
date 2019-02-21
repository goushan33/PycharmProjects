import urllib,json
from urllib import request

#利用urllib读取JSON，然后将JSON解析为Python对象：
def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
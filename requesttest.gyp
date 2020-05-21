# -*- coding: utf-8 -*-
from urllib import request
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        return  data.decode('utf-8')

def fetch_data1(url):
    with request.urlopen(url) as f:
        data = f.read()
        return  data

if __name__ == "__main__":
    data1 = fetch_data('https://yesno.wtf/api')
    data2 = fetch_data1('https://yesno.wtf/api')   
    # print(data1['query']['results']['channel']['location']['city'])
    print(data1)
    print(data2)
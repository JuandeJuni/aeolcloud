import requests
import time 
import json

cookies = {
    'doSomethingOnlyOnce': 'true',
    'www': 'w03|ZVXOo|ZVXOo',
    '__utma': '232416333.1648873574.1697629956.1697629956.1700122111.2',
    '__utmc': '232416333',
    '__utmz': '232416333.1700122111.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '_gid': 'GA1.2.1456415032.1700122111',
    '_ga': 'GA1.2.1648873574.1697629956',
    '_gat': '1',
    '__utmb': '232416333.6.10.1700122111',
    'laravel_session': 'eyJpdiI6IjkrSERDV1NNaHdvN1VRUEQ1b2w5OWc9PSIsInZhbHVlIjoiMjRVOFB2ekh2dlNTUW9VVFl0bzgyRHBOcXgrK1NXVEpyTDZsQ2VwaWRRVHo5RmlseUcxaE1DZUcyTUJmQTVzNFRLZ1pMRDFWY0pzaE12QWtNajR3SkE9PSIsIm1hYyI6ImViMTFmY2M5M2M5YjExNTQ5NmNkZDgwZGZhY2NkM2JmY2QwMjIzZDFmYTIzYjY5NDUzMzQ5ZmRkNzc5YjkwN2UifQ%3D%3D',
    '_ga_KZXBV0X7EM': 'GS1.1.1700122111.2.1.1700122187.52.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'es-ES,es;q=0.9,de;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'doSomethingOnlyOnce=true; www=w03|ZVXOo|ZVXOo; __utma=232416333.1648873574.1697629956.1697629956.1700122111.2; __utmc=232416333; __utmz=232416333.1700122111.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _gid=GA1.2.1456415032.1700122111; _ga=GA1.2.1648873574.1697629956; _gat=1; __utmb=232416333.6.10.1700122111; laravel_session=eyJpdiI6IjkrSERDV1NNaHdvN1VRUEQ1b2w5OWc9PSIsInZhbHVlIjoiMjRVOFB2ekh2dlNTUW9VVFl0bzgyRHBOcXgrK1NXVEpyTDZsQ2VwaWRRVHo5RmlseUcxaE1DZUcyTUJmQTVzNFRLZ1pMRDFWY0pzaE12QWtNajR3SkE9PSIsIm1hYyI6ImViMTFmY2M5M2M5YjExNTQ5NmNkZDgwZGZhY2NkM2JmY2QwMjIzZDFmYTIzYjY5NDUzMzQ5ZmRkNzc5YjkwN2UifQ%3D%3D; _ga_KZXBV0X7EM=GS1.1.1700122111.2.1.1700122187.52.0.0',
    'Origin': 'https://cloud.aeolservice.es',
    'Pragma': 'no-cache',
    'Referer': 'https://cloud.aeolservice.es/repaso_offline/5/126',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    '_token': 'JKhDJ73Mrjge54fNyC2oWPoXUElJJjDSGvktRrTk',
    'date': int(time.time()),
}
data = []
for i in range(101,134):
    response = requests.post(f'https://cloud.aeolservice.es/api/test/5/{i}/3/30', params=params, cookies=cookies, headers=headers)
    data.append(response.json())
with open('data.json', 'w') as f:
    json.dump(data, f)
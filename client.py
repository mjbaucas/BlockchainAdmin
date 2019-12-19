import requests
import json
import time

url = ' http://localhost:3000/send'
url2 = 'https://8db81646-9af2-4595-ba2f-424c1433fdd3.mock.pstmn.io/send'
data = {'ID': 10, 'timestamp': int(round(time.time() * 1000))}

x = requests.post(url, json=json.dumps(data), headers={'Content-Type': 'application/json', 'X-Api-Key' : ''})
print(x.text)
print(x.elapsed.total_seconds())
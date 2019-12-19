import requests
import json
import time

url = ' http://10.11.252.136:3000/send'
url2 = 'https://8db81646-9af2-4595-ba2f-424c1433fdd3.mock.pstmn.io/send'
data = {'ID': 10, 'timestamp': int(round(time.time() * 1000))}

for x in range(0,1000):
	x = requests.post(url, json=json.dumps(data), headers={'Content-Type': 'application/json', 'X-Api-Key' : ''})
	elapsed = x.elapsed.total_seconds()
	print(x.text)
	print(elapsed)

	f = open('4DeviceLocalA.txt', 'a')
	f.write(str(elapsed) + '\n')
	f.close()
	
	x = requests.post(url2, json=json.dumps(data), headers={'Content-Type': 'application/json', 'X-Api-Key' : ''})
	elapsed = x.elapsed.total_seconds()
	print(x.text)
	print(elapsed)

	f = open('4DevicePostmanA.txt', 'a')
	f.write(str(elapsed) + '\n')
	f.close()

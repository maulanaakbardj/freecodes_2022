import requests 

req = requests.get('https://ip.seeip.org/jsonip')
jsn = req.json()['ip']
print('your ip :',jsn)

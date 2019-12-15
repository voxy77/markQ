import requests

with open('file1.xml', 'rb') as f:
    headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    r = requests.post('https://qluqf59wsh.execute-api.eu-west-2.amazonaws.com/test/forward-to-bucket/', data={'pxeconfig': f.read()}, headers = headers)
    print(r.text)

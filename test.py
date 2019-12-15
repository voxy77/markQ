import requests

payload = '{"test" : "invoke"}'

r = requests.post('https://soiaxblv70.execute-api.eu-west-2.amazonaws.com/v1/post-json', data=payload)

print (r.text)
#assert r.status_code == 200
print(r.status_code)
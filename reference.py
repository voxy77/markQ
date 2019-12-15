# getting an asserting response code from api gateway
import boto as boto
import requests
#url = ' https://95bnogtxy8.execute-api.eu-west-2.amazonaws.com/test?id=6'
#r = requests.get(url)
#print(r.text)
#print(r.status_code)
#assert r.status_code == 200

# 3 lines to upload a file direct to S3
#import boto3
#s3 = boto3.resource('s3')
#s3.Bucket('firstqtooltest').upload_file("file1.xml", "file1.xml")

# PUT data into and existing file direct to s3
#payload = {'username': 'bob', 'email': 'bob@bob.com'}
#r = requests.put("https://firstqtooltest.s3.eu-west-2.amazonaws.com/file1.txt", data=payload)

# PUT data to an endpoint via an API Gateway
#payload = {'username': 'bob', 'email': 'bob@bob.com'}
#r = requests.put('https://k1ekq39i60.execute-api.eu-west-2.amazonaws.com/test', data=payload)
#print(r.status_code)




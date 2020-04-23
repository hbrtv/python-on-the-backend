import requests

url = "http://localhost:8080/"

files = [
    ('files', ('test1.png', open('test1.png', 'rb'), 'png')),
    ('files', ('test2.png', open('test2.png', 'rb'), 'png')),
    ('files', ('test3.png', open('test3.png', 'rb'), 'png'))
]

#files = {'files': open('test1.png', 'rb')}

#r = requests.post(url, files=files)
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

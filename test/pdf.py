import requests

url = 'http://localhost:3000/pdf'
files = {'file': open('public/10711127.pdf', 'rb')}

response = requests.post(url, files=files)
print(response.json())
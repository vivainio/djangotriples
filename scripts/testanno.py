import requests,json

payload = {
	'@id' : "com.myapp",
	'rating' : "5.5",
	'comment' : 'Rubbish!'
}

headers = {'Content-type': 'application/json' }

pjson = json.dumps(payload)

print "Posting",pjson
r = requests.post("http://localhost:8000/api/v1/put/", data = pjson, headers = headers)

print r
print r.text
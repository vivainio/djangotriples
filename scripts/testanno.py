import requests,json

payload = {
	'@id' : "com.myapp",
	'rating' : "5.5",
	'comment' : 'Rubbish!'
}

headers = {'Content-type': 'application/json' }

pjson = json.dumps(payload)

url = "http://djangotriples.herokuapp.com")

# local testing

# url = "http://localhost:8000"
print "Posting",pjson
r = requests.post(url + "/api/v1/put/", data = pjson, headers = headers)

print r
print r.text
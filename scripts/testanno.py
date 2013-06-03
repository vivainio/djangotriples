import requests,json

payload = {
	'@id' : "com.myapp",
	'rating' : "5.5",
	'comment' : 'Rubbish!'
}

headers = {'Content-type': 'application/json' }

pjson = json.dumps(payload)

pjson = """{ "@id": "Feedback Test Version 1.0.0 for Nokia Asha", "username": "Dggdd", "rating": 5, "comments": "Cffx" }"""


#"""{ "@id" : "FeedbackTest Version null for Nokia Asha", "username" : "Gdfdgrxtd", "rating" : "4", "comments" : "Dgfdffgff" }"""

 

url = "http://djangotriples.herokuapp.com"

# local testing

#url = "http://localhost:8000"
print "Posting",pjson
r = requests.post(url + "/api/v1/put/", data = pjson, headers = headers)

print r
print r.text

r = requests.get(url + "/api/v1/dump/")
print r
print r.text

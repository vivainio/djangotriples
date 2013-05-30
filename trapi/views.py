# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import json,pprint

from django.core import serializers

def jsonresp(obj):
    out = json.dumps(obj, indent=2)
    return HttpResponse(out, mimetype="application/json")


def parsepost(req):
    r = req.POST
    raw = req.raw_post_data
    d = json.loads(raw)
    return d



def put(request, subject):
	print "put", subject


	return HttpResponse("OK")

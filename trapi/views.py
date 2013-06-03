# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import json,pprint

from django.core import serializers
from trapi.models import *


class TripleController:
	def __init__(self):
		pass

	def get_elem(self, tab, name):
		el = tab.objects.get_or_create(name=name)
		return el[0]


	def put_entry(self, entry):
		assert '@id' in entry
		
		sub = self.get_elem(Subject, entry['@id'] )
		at = AnnotationTx.objects.create()
		for k,v in entry.items():
			if k.startswith('@'):
				# keys starting with @ are special				
				continue
			pred = self.get_elem(Predicate, k)
			t = Triple(s = sub,
				p = pred, 
				o = v,
				tx = at)
			t.save()

		at.save()



def jsonresp(obj):
    out = json.dumps(obj, indent=2)
    return HttpResponse(out, mimetype="application/json")


def parsepost(req):
    r = req.POST
    raw = req.body
    print "Raw post data", raw
    d = json.loads(raw)
    return d

def put(request):	
	po = parsepost(request)
	print po
	tc = TripleController()
	tc.put_entry(po)


	return HttpResponse("OK")

def dump(request):
	def a(s): return list(s.objects.all())

	out = serializers.serialize('json', a(Triple) + a(Subject) + a(Predicate))

	return HttpResponse(out, mimetype="application/json")	

def query(request):
	pass



from django.db import models

from django.contrib import admin
# Create your models here.


class Subject(models.Model):
	name = models.CharField(max_length = 200)

class Predicate(models.Model):
	name = models.CharField(max_length = 200)

class AnnotationTx(models.Model):
	tstamp = models.DateTimeField(auto_now_add = True)


class Triple(models.Model):
	tx = models.ForeignKey(AnnotationTx)
	s = models.ForeignKey(Subject)
	p = models.ForeignKey(Predicate)
	o = models.TextField()

admin.site.register(Subject)
admin.site.register(Predicate)
admin.site.register(AnnotationTx)
admin.site.register(Triple)


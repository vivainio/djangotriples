from django.db import models

# Create your models here.

class Subject(models.Model):
	name = models.CharField(max_length = 200)

class Triple(models.Model):
	subject = models.ForeignKey(Subject)
	predicate = models.CharField(max_length = 200)
	object = models.CharField(max_length = 200)


from __future__ import unicode_literals

from django.db import models

class CoreJava(models.Model):
	cjq = models.CharField(max_length=250)
	cja = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.cjq


class BasicJava(models.Model):
	bjq = models.CharField(max_length=250)
	bja = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.bjq


class AdvancedJava(models.Model):
	ajq = models.CharField(max_length=250)
	aja = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.ajq


class CProg(models.Model):
	cpq = models.CharField(max_length=250)
	cpa = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.cpq

class DataStructure(models.Model):
	dsq = models.CharField(max_length=250)
	dsa = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.dsq


class Dbms(models.Model):
	dbq = models.CharField(max_length=250)
	dba = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.dbq


class ComputerNetwork(models.Model):
	cnq = models.CharField(max_length=250)
	cna = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.cnq


class OperatingSystem(models.Model):
	osq = models.CharField(max_length=250)
	osa = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.osq


class Unix(models.Model):
	uxq = models.CharField(max_length=250)
	uxa = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.uxq


class Comment(models.Model):
	email = models.EmailField()
	comments = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email
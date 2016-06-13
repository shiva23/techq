from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from .models import *
from .forms import CommentForm
import requests


def home(request):
	content ={}
	template="home.html"
	return render(request, template, content)

def javadef(request):
	content ={}
	template="java.html"
	return render(request, template, content)


def contactdef(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(request,"contact.html")
	content ={"form": form, }
	return render(request,"contact.html",content)


def commentdef(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(request,"contact.html")
	content ={"form": form}
	return render(request,"comment.html",content)



def corejavadef(request):

	qs_list=CoreJava.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(cjq__icontains=query) | Q(cja__icontains=query))

	paginator = Paginator(qs_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'corejava.html', content)



def basicjavadef(request):

	qs_list=BasicJava.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(bjq__icontains=query) | Q(bja__icontains=query))

	paginator = Paginator(qs_list, 5)

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'basicjava.html', content)



def advancedjavadef(request):

	qs_list=AdvancedJava.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(ajq__icontains=query) | Q(aja__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'advancedjava.html', content)


def cprogdef(request):

	qs_list=CProg.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(cpq__icontains=query) | Q(cpa__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'cprog.html', content)


def datastructuredef(request):

	qs_list=DataStructure.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(dsq__icontains=query) | Q(dsa__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'datastructure.html', content)


def computernetworkdef(request):

	qs_list=ComputerNetwork.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(cnq__icontains=query) | Q(cna__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'computernetwork.html', content)


def dbmsdef(request):

	qs_list=Dbms.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(dbq__icontains=query) | Q(dba__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'dbms.html', content)



def operatingsystemdef(request):

	qs_list=OperatingSystem.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(osq__icontains=query) | Q(osa__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'operatingsystem.html', content)


def unixdef(request):

	qs_list=Unix.objects.all()
	query = request.GET.get('q')
	if query:
		qs_list = qs_list.filter(Q(uxq__icontains=query) | Q(uxa__icontains=query))

	paginator = Paginator(qs_list, 5) 

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		qs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		qs = paginator.page(paginator.num_pages)

	content={'obj':qs,}
	return render(request, 'unix.html', content)



def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')
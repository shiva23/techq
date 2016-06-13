"""tiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from question import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^java/', views.javadef),
    url(r'^corejava/', views.corejavadef),
    url(r'^basicjava/', views.basicjavadef),
    url(r'^advancedjava/', views.advancedjavadef),
    url(r'^cprog/', views.cprogdef),
    url(r'^datastructure/', views.datastructuredef),
    url(r'^dbms/', views.dbmsdef),
    url(r'^computernetwork/', views.computernetworkdef),
    url(r'^operatingsystem/', views.operatingsystemdef),
    url(r'^unix/', views.unixdef),
    url(r'^contact/', views.contactdef),
    url(r'^comment/', views.commentdef),
    url(r'^', views.home),
    url(r'^home/', views.home),

]


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
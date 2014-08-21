from django.conf.urls import patterns, include, url
from visflow import views

urlpatterns = patterns('',
    url(r'^viewflow/$', views.visflowmap, name='visflowmap'),
)
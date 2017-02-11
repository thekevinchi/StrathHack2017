from dank_app import views
from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'result/$', views.result, name='result'),
    url(r'speech/$', views.speech, name='speech'),
]

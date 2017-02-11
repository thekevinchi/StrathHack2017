from dank_app import views
from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'speech$', views.speech, name='speech'),
]

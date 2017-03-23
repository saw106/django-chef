from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^for/testing/purposes/only/$', views.chef_test, name='chef_test'),
]

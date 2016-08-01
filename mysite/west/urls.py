from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','west.views.first_page'),
	url(r'^star/','west.views.star'),
	url(r'^temp/','west.views.templay'),
)

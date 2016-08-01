from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^logout/','users.views.user_logout'),
	url(r'^login/','users.views.user_login'),
) 
from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('accounts.views',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)

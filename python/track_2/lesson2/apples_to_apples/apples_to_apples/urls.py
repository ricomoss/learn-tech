from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^common/', include('common.urls', namespace='common')),
)

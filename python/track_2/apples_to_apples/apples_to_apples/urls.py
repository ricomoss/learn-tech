from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)

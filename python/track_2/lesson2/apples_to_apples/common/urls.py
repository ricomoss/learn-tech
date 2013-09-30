from django.conf.urls import patterns, url

from common import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^use-template/', views.pop_template, name='pop_template'),
    url(r'^person-form/', views.person_form, name='person_form'),
    url(r'^person-form-from-model/', views.person_form, name='person_form'),
)

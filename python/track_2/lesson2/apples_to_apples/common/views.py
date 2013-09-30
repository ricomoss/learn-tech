from django.http import HttpResponse
from django.shortcuts import render_to_response

from common import forms as common_forms


def index(request):
    response = 'You are at the index page'
    return HttpResponse(response)


def pop_template(request):
    context = {'name': 'Rico Cordova'}
    template = 'common/base.html'
    return render_to_response(template, context)


def person_form(request):
    form = common_forms.PersonForm()
    template = 'common/person_form.html'
    context = {'form': form}
    return render_to_response(template, context)


def person_form_from_model(request):
    form = common_forms.PersonFormFromModel()
    template = 'common/person_form.html'
    context = {'form': form}
    return render_to_response(template, context)

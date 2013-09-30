from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from accounts.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('accounts:index'))

    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if not request.POST.get('remember', False):
                    request.session.set_expiry(0)
                auth.login(request, user)
                return HttpResponseRedirect(reverse('accounts:index'))
            else:
                messages.error(request, _('Your account is not active'))
        else:
            messages.error(request, _('Invalid username or password'))

    return render_to_response(
        'accounts/login.html', {}, RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

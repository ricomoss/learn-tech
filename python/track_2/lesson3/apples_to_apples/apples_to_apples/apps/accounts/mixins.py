from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


# class PermissionsRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.profile.is_permitted(self.permissions_required):
#             raise PermissionDenied
#         return super(PermissionsRequiredMixin, self).dispatch(
#             request, *args, **kwargs)

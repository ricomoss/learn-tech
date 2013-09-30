# from __future__ import unicode_literals
#
# from django import forms
# from django.contrib.auth.models import User
#
# from accounts import constants
#
#
# class UserForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50, required=True)
#     last_name = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(max_length=50, required=True)
#     username = forms.RegexField(
#         regex=r'^[\w.@+-]+$', max_length=50, required=True)
#     access_level = forms.ChoiceField(choices=constants.PERMISSION_CHOICES)
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         )
#
#     def save(self, commit=True):
#         user = super(UserForm, self).save()
#         profile = user.profile
#         profile.permission = self.cleaned_data['access_level']
#         profile.save()
#
#         return user

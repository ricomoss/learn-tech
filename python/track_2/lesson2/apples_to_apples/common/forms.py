from django import forms

from common import models as common_models


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25, required=False)
    hair_color = forms.CharField(max_length=10, required=False)
    eye_color = forms.CharField(max_length=10)
    age = forms.IntegerField()
    height = forms.CharField(max_length=6)
    favorite_animal = forms.CharField(max_length=25, required=False)
    number_of_animals = forms.IntegerField(required=False)


class PersonFormFromModel(forms.ModelForm):
    def meta(self):
        model = common_models.Person
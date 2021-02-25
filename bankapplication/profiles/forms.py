from django.forms import ModelForm
from django import forms
from profiles.models import createProfileModel


class DateInput(forms.DateInput):
    input_type = 'date'




class createProfileForm(ModelForm):
    # user = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = createProfileModel
        fields = "__all__"
        widgets = {'user': forms.HiddenInput(),
                   'date_of_birth': DateInput(),
                   }

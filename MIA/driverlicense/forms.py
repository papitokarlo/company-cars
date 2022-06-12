from django import forms
from django.forms import ModelForm
from .models import *

class carForm(ModelForm):
    class Meta:
        model = Cars
        fields = ('number', 'color', 'marck', 'model', 'date', 'image')

        labels = {
            'number' : '',
            'color' : '',
            'marck' : '',
            'model' : '',
            'number' : '',
            'image' : 'Choose image for your car',
        }

        widgets = {
            'number' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number: XX000XX'}),
            'color' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color:red'}),
            'marck' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'marck'}),
            'model' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'model'}),
            'date' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'date:13/09/2001'}),
            'image' : forms.ClearableFileInput(),
        }

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, car):
        return '%s' % car.number

class personForm(ModelForm):
    class Meta:
        model = Person
        fields = ('selfid', 'name', 'lastname', 'father', 'birth', 'car')

        labels = {
            'selfid' : '',
            'name' : '',
            'lastname' : '',
            'father' : '',
            'birth' : '',
            'car' : '',
        }

        widgets = {
            'selfid' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID N:00000000000'}),
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),
            'father' : forms.TextInput(attrs={'class':'form-control', 'placeholder':"Father's name"}),
            'birth' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'birth date:13/09/2001'}),
        }
        car= CustomMMCF(queryset=Cars.objects.all(),
            widget = forms.CheckboxSelectMultiple
        )

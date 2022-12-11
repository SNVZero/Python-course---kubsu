from .models import *
from django.forms import ModelForm, TextInput, DateInput


class PacientForm(ModelForm):
    class Meta:
        model = Pacient
        fields = ['NamePac', 'Policy', 'Birth', 'Location']

        widgets = {
            'NamePac': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'ФИО'
            }),
            'Policy': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Номер страхового полиса',
            }),
            'Birth': DateInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Дата рождения'
            }),
            'Location': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Место жительства'
            }),
        }


class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['Diagnos', 'Severity']

        widgets = {
            'Diagnos': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Диагноз'
            }),
            'Severity': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Степень тяжести'
            }),
        }

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ['MethodOfThreatment', 'DurationOfTreat']

        widgets = {
            'MethodOfThreatment': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Метод лечения'
            }),
            'DurationOfTreat': TextInput(attrs={
                'class': 'contnent__elem',
                'placeholder': 'Срок лечения'
            }),
        }

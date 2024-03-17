from django import forms
'''
https://docs.djangoproject.com/en/5.0/topics/forms/
https://docs.djangoproject.com/en/5.0/ref/forms/fields/
https://docs.djangoproject.com/en/5.0/ref/forms/api/
'''
class AbcForm(forms.Form):

    content = forms.CharField(label='Формулировка задачи', initial="Равна ли C сумме A и B? Равна ли C сумме A и B?",required=True, widget=forms.Textarea())
    a = forms.IntegerField(label='Значение A', required=False, initial=1, widget=forms.NumberInput())
    b = forms.IntegerField(label='Значение B', initial=2, widget=forms.NumberInput())
    c = forms.IntegerField(label='Значение C', initial=3)

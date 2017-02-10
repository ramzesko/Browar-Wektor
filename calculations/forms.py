from django import forms


class CarbonationCalculator(forms.Form):
    carbonation = forms.FloatField(label='Oczekiwane nagazowanie', max_value=4)
    temperature = forms.IntegerField(label='Temperatura butelkowania', max_value=50)
    volume = forms.FloatField(label='Objętość piwa')

from django import forms


class CarbonationCalculator(forms.Form):
    carbonation = forms.FloatField(label='Oczekiwane nagazowanie [vol.]',
                                   min_value=0.1,
                                   max_value=4,
                                   initial=2,
                                   widget=forms.NumberInput(attrs={'step': '0.1'}),
                                   help_text='Zalecane nagazowanie między 1.8 a 2.5.',
                                   )
    temperature = forms.IntegerField(label='Temperatura piwa [st. Celsjusza]',
                                     min_value=1,
                                     max_value=50,
                                     initial=20,
                                     help_text='Wybierz temperaturę otoczenia podczas butelkowania.',
                                     )
    volume = forms.FloatField(label='Objętość piwa [L]',
                              min_value=1,
                              initial=20,
                              help_text='Objętość butelkowanego piwa w litrach.'
                              )

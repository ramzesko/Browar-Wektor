from django.shortcuts import render
from calculations.forms import CarbonationCalculator
from calculations.calculation_functions import carbonation


def carbonation_calc(request):
    if request.method == 'POST':
        form = CarbonationCalculator(request.POST)
        if form.is_valid():
            vol = form.cleaned_data['carbonation']
            temperature = form.cleaned_data['temperature']
            volume = form.cleaned_data['volume']
            result = carbonation(vol, temperature, volume)
            return render(request, 'calculations/carbonation_result.html', {'form': form, 'vol': vol, 'temperature': temperature, 'volume': volume, 'result': result})
    else:
        form = CarbonationCalculator()
    return render(request, 'calculations/carbonation.html', {'form': form})
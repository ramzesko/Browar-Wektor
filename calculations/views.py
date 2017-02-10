from django.shortcuts import render
from calculations.forms import CarbonationCalculator
from calculations.calculation_functions import carbonation

# def carbonation(request):
#     return render(request, 'calculations/carbonation.html', {})

def carbonation_calc(request):
    if request.method == 'POST':
        form = CarbonationCalculator(request.POST)
        if form.is_valid():
            desired_carbonation = form.cleaned_data['carbonation']
            temperature = form.cleaned_data['temperature']
            volume = form.cleaned_data['volume']
            # tu wywołaj funkcję obliczającą na argumentach desired_carbonation, temparature i volume
            result = carbonation(desired_carbonation, temperature, volume)
            return render(request, 'calculations/carbonation_result.html', {'form': form, 'desired_carbonation': desired_carbonation, 'temperature': temperature, 'volume': volume, 'result': result})
    else:
        form = CarbonationCalculator()
    return render(request, 'calculations/carbonation.html', {'form': form})
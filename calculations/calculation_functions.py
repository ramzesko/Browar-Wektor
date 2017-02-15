def carbonation(vol, temperature, volume):
    sugar = 15.195 * volume / 3.78541178 * (vol - dissolved(temperature))
    return round(sugar, 2)

def dissolved(temperature):
    return 3.0378 - (0.050062 * (temperature*9/5+32)) + (0.00026555 * (temperature*9/5+32)**2)
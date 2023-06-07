# Create a Python program that converts a temperature from Fahrenheit to Celsius.
# The user should enter the temperature in Fahrenheit, and the program should print
# the equivalent temperature in Celsius.

Temperature = float(input('Ingrese la temperatura en grados farenheit '))

print ("La temperatura en grados celsius es {}".format((Temperature - 32.0) * 5/9))
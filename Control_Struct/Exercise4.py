# Create a Python program that checks if a given number is prime or not. The user
# should input a number, and the program should print whether it is prime or not.

def fact(number):
    number_fact = 1

    for i in range(1, number+1):
        number_fact *= i
    
    return number_fact

number = int(input('Ingrese un número para validar si es número primo'))

number_factorial = fact(number-1)
number_fact1=number_factorial + 1
print(number_fact1)

comparacion = (number_fact1/number)

if comparacion % 1 == 0:
    print ('el número ingresado es primo')
else:
    print('el número ingresado no es primo')

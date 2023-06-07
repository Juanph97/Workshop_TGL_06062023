# Write a Python function called find_maximum that takes a list of numbers as input
# and returns the maximum number from the list.

def find_maximun(list_number):

    number_max = max (list_number)
    return number_max

list_number = [1,101,3,6,7,89,98]

number =find_maximun(list_number)

print("el número máximo de la lista es : ", number)
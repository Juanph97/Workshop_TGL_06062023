# # Create a Python decorator called timer that measures the time taken to execute a
# # function. Use this decorator on a function that sorts a list of random numbers and
# # prints the sorted list.

# import time
# import random

# def timer(func):
#     def total_time(list_random_number):
#         time_1 = time.time()
#         result = func(list_random_number)
#         time_2 = time.time()
#         execution_time = time_2 - time_1
#         print(f"function execution time {func.__name__}: {execution_time} seconds")
#         return result
#     return total_time

# @timer # Se posiciona antes de la función a la que se requiere medir el tiempo de ejecución.
# def ordenar_lista(lista):
#     lista.sort()
#     print("Lista ordenada:", lista)

# lista_numeros = random.sample(range(1000), 30)

# ordenar_lista(lista_numeros) # Llamado de la función decorada

#Iteradores

my_list = [1,2,3,4,5]
my_list[1:4] = [10,20,30]
print(my_list)
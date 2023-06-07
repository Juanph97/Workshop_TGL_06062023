#Write a Python program that prints the first 10 Fibonacci numbers using a loop

Fibonacci = [0,1]

for i in range(2,12):
    n = Fibonacci[i-1]+Fibonacci[i-2]
    Fibonacci.append(n)


print(Fibonacci) 
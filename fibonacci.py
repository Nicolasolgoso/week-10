def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)


while True:
    numero = int(input("¿Qué número quieres calcular?"))
    print(fib(numero))

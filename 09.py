#Imprimir los números impares desde el 1 hasta el número ingresado
print ("Imprimir los números impares desde el 1 hasta el número ingresado")
num = int(input("Ingrese un número entero positivo: "))
n = 1
while n <= num:
    if n % 2 != 0:
        print (n)
    n += 1
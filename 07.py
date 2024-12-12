#Sumar los digitos de un número
print ("Sumar los digitos de un número")
num = int(input("Ingresa un número entero positivo: "))
suma = 0
while num > 0:
    suma += num % 10
    num //= 10
print ("Suma de los digitos", suma)
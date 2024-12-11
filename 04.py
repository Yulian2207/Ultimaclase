#Imprimir los primeros diez números pares.
print ("imprimir los primeros 10 números pares")

n = int (input("Ingresa el número desde donde empezar a buscar pares: "))
contador = 0

while contador < 10:
    if n % 2 == 0:
        print (n)
        contador += 1
    n += 1

#Calcular el factorial del número ingresado

print ("Calcular el factorial del número ingresado")
num = int (input("Calcular el factorial del número ingresado"))

resultado = 1
while num > 0:
    resultado *= num
    num -= 1
print("Factorial:", resultado)

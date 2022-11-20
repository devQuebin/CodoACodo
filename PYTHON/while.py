cont= 0
suma= 0
while cont < 5:
    num= int(input("Ingrese un número: "))
    suma = suma + num # Acumulamos, es equivalente suma += num
    cont = cont + 1 # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)
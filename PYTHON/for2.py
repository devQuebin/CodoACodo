suma= 0
for cont in range(1,4):
    num= int(input("Ingrese un número: "))
    suma = suma + num # Acumulamos, es equivalente suma += num
print("La suma es:", suma)
print("El promedio es:", suma/cont)
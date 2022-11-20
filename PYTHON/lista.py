listas=[] #lista vacia
lista2=["Uno", 2, True, 9.8]
#print(lista2)

frutas=["Banana","Manzana","Mango","Pera","Manzana"]
print(frutas)
print(frutas[1])
frutas[2]="Frutilla"
print(frutas)

frutas2=["Durazno","Kiwi","Sandia"]

frutas3=frutas+frutas2
#print(frutas3)

frutas3.append("Mora")
print(frutas3)

lista = [2,3,4,5,6]
suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]
print(suma) 
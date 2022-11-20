diccionario = {1: 'uno', 2:'dos', 3:'tres'}
print(diccionario.keys())

for i in diccionario.keys():
    print(diccionario[i])

    
for clave, valor in diccionario.items():
    print(clave, ':', valor, end= '; ')
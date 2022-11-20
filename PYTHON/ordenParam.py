def imprimir_mensaje_N_veces(n, m):
    for i in range(n):
        print(m)
        
mensaje = input("Mensaje: ")
veces = int(input("Nro. de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces, mensaje)
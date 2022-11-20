nota=int(input("ingresar nota"))

if nota > 10:
  print("Error al cargar la nota");
elif nota >= 9:
  print("Sobresaliente")
elif nota >=7:
  print("Notable")
elif nota >=6:
  print("Bien")
elif nota >=5:
  print("Suficiente")
elif nota >=3:
  print("Insuficiente")
elif nota >= 0:
  print("Muy deficiente")
else: 
  print("Error al cargar la nota")
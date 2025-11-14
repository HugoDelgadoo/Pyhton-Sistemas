nombres = []
a = False
contador = 0
while(a == False):

    nombre = input("Dime nombres")
    if nombre.lower() == "fin":
        a = True
    else:
        nombres.append(nombre)
        contador = contador + 1

print(nombres)
print(f"numero de nombres: {contador}")




if len(nombres) > 0:
    nombre_buscar = input("\n¿Qué nombre quieres buscar? ")
    veces = nombres.count(nombre_buscar)
    print(f"El nombre {nombre_buscar} aparece {veces} veces")
else:
    print("ese nombre no esta o la lista esta vacia")


if nombre_buscar in nombres:
   nombres.index(nombre_buscar)
   nombres.remove(nombre_buscar)
   print(f"lista actualizada {nombres}")
else:
    print("no esta ese nombre en la lista")

nombres = {"Pablo", "Juan", "Arjama", "Daniel"}
acabar = True
#1
while acabar:
    nombre = input("dime nombres de personas en el taller(fin para salir)")
    if nombre.lower() == "fin":
        acabar = False
        break
    if nombre == "":
        print("no puede estar vacio el nombre")
        continue
    if nombre.startswith(" ") or nombre.endswith(" "):
        print("el nombre no puede empezar ni acabar con espacios")
        continue
    nombres.add(nombre)
    print("nombre añadido")


#2
while acabar:
    cadena = input("dime nombres para añadir")
    lote = {n.strip() for n in cadena.split(",") if n.strip() != ""}
    nombres.update(lote)
    print("nombres añadidos correctamente")


#3
copia = nombres.copy()
print("nombres copiados")


#4
eliminar = input("dime el nombre a dar de baja").strip()
if eliminar in nombres:
    nombres.remove(eliminar)
    print("nombre eliminado")
else:
    print("ese nombre no se encuentra en la lista")


#5
consulta = input("dime un nombre a buscar").strip()
if consulta in nombres:
    print("ese nombre si esta en la lista")
else:
    print("ese nombre no esta en la lista")


#6
grupo = {"Ana", "Luis", "Pablo"}
print("Grupo a comprobar:", grupo)

if nombres.intersection(grupo):
    print("Alguien del grupo está inscrito")
else:
    print("Nadie del grupo está inscrito")


#7
print("\nTotal de inscritos:", len(nombres))
print("Lista ordenada:")
print(sorted(nombres))
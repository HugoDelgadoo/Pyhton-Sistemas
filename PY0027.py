usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan", "Marta"}

administradores.discard("Juan")

administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario} es administrador")
    else:
        print(f"{usuario} no es administrador")

print("Pizzeria la Beata")
dinero = float(input("cuanto dinero tienes?"))
p1 = 9.00
p2 = 8.66
p3 = 5.54

print("Pizzas disponibles:")
print(f"Margarita : {p1}")
print(f"4 quesos: {p2}")
print(f"Barbacoa: {p3}")

opcion = int(input("\nElige una pizza (1-3): "))

if opcion == 1:
    precio_pizza = p1
    nombre_pizza = "Margarita"
elif opcion == 2:
    precio_pizza = p2
    nombre_pizza = "4 Quesos"
elif opcion == 3:
    precio_pizza = p3
    nombre_pizza = "Barbacoa"
else:
    print("eso no es una opcion valida")
    exit()
restante = dinero - precio_pizza
print(f"Has elegido: {nombre_pizza} {precio_pizza}")
print(f"Te queda: {round(restante, 2)} euros")

precio_extra1 = 0.25
precio_extra2 = 0.5
precio_extra3 = 0.75

extras = []
precio_extras = 0

print("Ingredientes disponibles")
print(f"1. Mas de queso - {precio_extra1}$")
print(f"2.  Mas salsa bbq- {precio_extra2}$")
print(f"3. Champiñones - {precio_extra3}$")
print("0. No añadir más extras")


while True:
    extra = int(input("elige un extra (0-3)"))
    if extra == 0:
        break
    elif extra == 1:
        extras.append(("mas de queso", precio_extra1))
        precio_extras += precio_extra1
    elif extra == 2:
        extras.append(("mas salsa bbq", precio_extra2))
        precio_extras += precio_extra2
    elif extra == 3:
        extras.append(("Champiñones", precio_extra3))
        precio_extras += precio_extra3
    else:
        print("Eso no es una opcion")

total = round(precio_pizza + precio_extras,2)

if(dinero < total):
    print("no tienes dinero suficiente para eso:")
    exit()

cambio = round(dinero-total,2)

print("--- Su Pedido ---")
print(f"El total de su pedido es {total}")
print(f"Su cambio de {dinero} es: {cambio} ")
print(f"-{nombre_pizza} {precio_pizza}")
for nombre, precio in extras:
    print(f"- {nombre} {precio}$")

print("\nGracias por su visita")

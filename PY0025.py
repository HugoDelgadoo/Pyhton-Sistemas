menu = "Menu, elija una de las siguientes opciones marcando su número: \n" \
       "1. Imprimir alfabeticamente en orden ascendente \n" \
       "2. Imprimir alfabeticamente en orden descendente \n" \
       "3. Añadir País\n" \
       "4. Eliminar Pais \n" \
       "5. Salir \n\n"

lista_paises = ["España", "Argentina", "Perú"]
numero_intentos = 0

while True:
    try:
        opcion = int(input(menu).strip())
    except ValueError:
        print("Error. Debe escribir un número del 1 al 5 con la opción elegida")
        continue
    else:
        match opcion:
            case 1: #imprimir ascendentemente
                print(sorted(lista_paises), end="\n\n")
            case 2:#imprimir descendentemente
                print(sorted(lista_paises, reverse=True), end="\n\n")
            case 3: #"Añadir país"
                if len(lista_paises) < 6:
                    pais = input("Que país desea añadir: ").strip().capitalize()
                    if not pais:
                        print("Debe indicar algún país \n")
                    elif pais in lista_paises:
                        print("El pais ya está en la lista \n")
                    else:
                        lista_paises.append(pais)
                        print(f"{pais} ha quedado añadido de la lista")
                        print("La lista de paises actualizada es: ", lista_paises, end="\n\n")
                else:
                    print("La lista ya tiene 6 países. Debe eliminar alguno antes de alñadir otro \n")
            case 4: #"Eliminar país"
                if len(lista_paises) > 0:
                    pais = input("Que país desea eliminar: ").strip().capitalize()
                    if pais and pais in lista_paises:
                        lista_paises.remove(pais)
                        print(f"{pais} ha quedado eliminado de la lista")
                        print("La lista de paises actualizada es: ", lista_paises, end="\n\n")
                    else:
                        print("Debe indicar algún país de la lista \n")
                else:
                    print("La lista de países ya está vacía, no se puede borrar ninguno \n")
            case 5:
                break
            case _:
                print("Error. Debe indicar un número del 1 al 5 con la opción elegida")
    finally:
        numero_intentos += 1
        print("El número total de ejecuciones es = " , numero_intentos, "\n")

    print("#" * 70, end="\n\n")

print(f"Gracias por usar el programa de paises. El numero total de intentos ha sido {numero_intentos} Un saludo.")
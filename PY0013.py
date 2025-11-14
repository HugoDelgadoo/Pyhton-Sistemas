import time

cadena = input("introduce una cadena: ")

caracter_original = input("Introduce el caracter que quieres reemplazar:\t")
caracter_nuevo = input("Introduce el caracter nuevo:\t")
if len(caracter_original) != 1 or len(caracter_nuevo) != 1:
    print("Solo puedes introducir un caracter")
    time.sleep(3)
    exit(1)
cadena_modificada = cadena.replace(caracter_original, caracter_nuevo)
print("Cadena modificada:", cadena_modificada)

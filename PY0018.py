registro = "zeréP nauJ,01"
registro_corregido = registro[::-1]
nota,nombre = registro_corregido.split(",")
print(f"{nombre} ha sacado una nota de {nota}")

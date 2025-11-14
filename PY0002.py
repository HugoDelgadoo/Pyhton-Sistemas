precios = [22.5, 10, 43.4, 20.6]
preciosDescuento = []

for i, precio in enumerate(precios, start=1):
    if i % 2 == 0:
        preciosDescuento.append(precio * 0.9)#me quedo con el 90% del precio del producto
    else:
        preciosDescuento.append(precio * 0.8)#me quedo con el 80% del precio del producto

for i in range(len(precios)):
    print(f"{i}. precio antes = {precios[i]:.2f}, precio ahora = {preciosDescuento[i]:.2f}")

matriz = [[1, 1, 1, 3],[2, 2, 2, 7],[3, 3, 3, 9],[4, 4, 4, 13]]

print("Matriz original:")
for fila in matriz:
    print(fila)

for i in range(len(matriz)):
    suma_tres_primeros = sum(matriz[i][:3])     
    matriz[i][3] = suma_tres_primeros

print("\nMatriz actualizada:")
for fila in matriz:
    print(fila)
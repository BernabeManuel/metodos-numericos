def gaussiana(matriz, vector):
    """
    Método de eliminación Gaussiana para resolver sistemas de ecuaciones lineales.

    Parámetros:
    matriz : matriz de coeficientes (lista de listas).
    vector : vector de términos independientes (lista).

    Retorna:
    Solución aproximada como lista, o None si no tiene solución.
    """
    n = len(matriz)

    # Eliminación hacia adelante
    for i in range(n):
        if matriz[i][i] == 0:
            print("Error: Cero en la diagonal principal.")
            return None

        for j in range(i+1, n):
            factor = matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                matriz[j][k] -= factor * matriz[i][k]
            vector[j] -= factor * vector[i]

    # Sustitución hacia atrás
    x = [0] * n
    for i in range(n-1, -1, -1):
        suma = sum(matriz[i][j] * x[j] for j in range(i+1, n))
        x[i] = (vector[i] - suma) / matriz[i][i]

    return x


# Ejemplo de uso:
if __name__ == "__main__":
    matriz = [
        [2, -1, 1],
        [3, 3, 9],
        [3, 3, 5]
    ]

    vector = [2, -1, 4]

    solucion = gaussiana(matriz, vector)

    if solucion:
        print("\nSolución del sistema:")
        for i, valor in enumerate(solucion, start=1):
            print(f"x{i} = {valor}")
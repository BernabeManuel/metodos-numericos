def imprimir_matriz(matriz, vector):
    """
    Imprime la matriz aumentada del sistema.
    """
    print("\nSistema actual:")
    for i in range(len(matriz)):
        fila = "\t".join(f"{num:8.4f}" for num in matriz[i])
        print(f"| {fila} | {vector[i]:8.4f}")
    print()


def gaussiana(matriz, vector):
    """
    Resuelve un sistema de ecuaciones lineales usando eliminación Gaussiana.

    Parámetros:
    matriz : lista de listas con los coeficientes (matriz cuadrada).
    vector : lista con los términos independientes.

    Retorna:
    lista con la solución o None si hay error.
    """
    n = len(matriz)

    for k in range(n):
        # Buscar el pivote (mayor valor absoluto en columna k para evitar errores numéricos)
        max_index = k
        max_value = abs(matriz[k][k])
        for i in range(k+1, n):
            if abs(matriz[i][k]) > max_value:
                max_value = abs(matriz[i][k])
                max_index = i
        if max_value == 0:
            print("Error: Matriz singular o sistema sin solución única.")
            return None
        # Intercambiar filas si es necesario
        if max_index != k:
            matriz[k], matriz[max_index] = matriz[max_index], matriz[k]
            vector[k], vector[max_index] = vector[max_index], vector[k]
            print(f"Se intercambiaron las filas {k} y {max_index} para mejorar el pivote.")
            imprimir_matriz(matriz, vector)

        # Eliminar variables
        for i in range(k+1, n):
            factor = matriz[i][k] / matriz[k][k]
            for j in range(k, n):
                matriz[i][j] -= factor * matriz[k][j]
            vector[i] -= factor * vector[k]

        imprimir_matriz(matriz, vector)

    # Sustitución hacia atrás
    solucion = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        suma = 0
        for j in range(i+1, n):
            suma += matriz[i][j] * solucion[j]
        if matriz[i][i] == 0:
            print("Error: División por cero durante la sustitución.")
            return None
        solucion[i] = (vector[i] - suma) / matriz[i][i]

    return solucion


def leer_sistema():
    """
    Solicita al usuario ingresar el sistema de ecuaciones.
    """
    while True:
        try:
            n = int(input("¿Cuántas incógnitas tiene el sistema? "))
            if n <= 0:
                print("El número de incógnitas debe ser positivo.\n")
                continue
            break
        except ValueError:
            print("Entrada inválida, por favor ingresa un número entero positivo.\n")

    matriz = []
    vector = []

    print("Introduce los coeficientes de la matriz y los términos independientes:")

    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                try:
                    val = float(input(f"Coeficiente a[{i+1}][{j+1}]: "))
                    fila.append(val)
                    break
                except ValueError:
                    print("Valor inválido, intenta de nuevo.")

        matriz.append(fila)

        while True:
            try:
                val = float(input(f"Término independiente b[{i+1}]: "))
                vector.append(val)
                break
            except ValueError:
                print("Valor inválido, intenta de nuevo.")

    return matriz, vector


def main():
    print("Resolución de sistemas de ecuaciones lineales por Eliminación Gaussiana\n")

    matriz, vector = leer_sistema()

    print("\nSistema inicial:")
    imprimir_matriz(matriz, vector)

    solucion = gaussiana(matriz, vector)

    if solucion is not None:
        print("\nSolución del sistema:")
        for i, val in enumerate(solucion, 1):
            print(f"x{i} = {val:.6f}")
    else:
        print("\nNo se pudo encontrar una solución única para el sistema.")


if __name__ == "__main__":
    main()

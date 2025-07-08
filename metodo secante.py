def secante(f, x0, x1, tol, max_iter):
    """
    Método de la secante para encontrar una raíz de la función f.

    Parámetros:
    f : función a evaluar.
    x0 : primer valor inicial.
    x1 : segundo valor inicial.
    tol : tolerancia (error permitido).
    max_iter : número máximo de iteraciones.

    Retorna:
    La raíz aproximada si converge, o None si no lo hace.
    """
    for i in range(max_iter):
        denominador = f(x1) - f(x0)
        if denominador == 0:
            print("Error: División por cero en la iteración", i+1)
            return None

        x2 = x1 - f(x1) * (x1 - x0) / denominador

        print(f"Iteración {i+1}: x = {x2}, f(x) = {f(x2)}")

        if abs(x2 - x1) < tol:
            print("\nRaíz encontrada con la tolerancia deseada.")
            return x2

        x0, x1 = x1, x2

    print("\nNo se alcanzó la convergencia después del número máximo de iteraciones.")
    return None


# Ejemplo de uso:
if __name__ == "__main__":
    def f(x):
        return x**3 - x - 2  # Cambiar esta función si es necesario

    # Valores iniciales
    x0 = 1.0
    x1 = 2.0
    tol = 1e-6
    max_iter = 100

    raiz = secante(f, x0, x1, tol, max_iter)

    if raiz is not None:
        print(f"\nRaíz aproximada: {raiz}")
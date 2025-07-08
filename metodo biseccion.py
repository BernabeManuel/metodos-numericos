def biseccion(f, a, b, tol, max_iter):
    """
    Método de bisección para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
    f : función a evaluar.
    a : límite inferior del intervalo.
    b : límite superior del intervalo.
    tol : tolerancia (error permitido).
    max_iter : número máximo de iteraciones.

    Retorna:
    La raíz aproximada si converge, o None si no lo hace.
    """
    if f(a) * f(b) >= 0:
        print("Error: La función debe tener signos opuestos en los extremos del intervalo.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)

        print(f"Iteración {i+1}: x = {c}, f(x) = {fc}")

        if abs(fc) < tol or abs(b - a) / 2 < tol:
            print("\nRaíz encontrada con la tolerancia deseada.")
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("\nNo se alcanzó la convergencia después del número máximo de iteraciones.")
    return None


# Ejemplo de uso:
if __name__ == "__main__":
    def f(x):
        return x**3 - x - 2  # Cambiar esta función si es necesario

    # Intervalo inicial
    a = 1.0
    b = 2.0
    tol = 1e-6
    max_iter = 100

    raiz = biseccion(f, a, b, tol, max_iter)

    if raiz is not None:
        print(f"\nRaíz aproximada: {raiz}")
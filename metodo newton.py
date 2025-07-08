def newton_raphson(f, df, x0, tol, max_iter):
    """
    Método de Newton-Raphson para encontrar una raíz de la función f.

    Parámetros:
    f : función a evaluar.
    df : derivada de la función.
    x0 : valor inicial.
    tol : tolerancia (error permitido).
    max_iter : número máximo de iteraciones.

    Retorna:
    La raíz aproximada si converge, o None si no lo hace.
    """
    x = x0
    for i in range(max_iter):
        dfx = df(x)
        if dfx == 0:
            print("Error: Derivada cero en la iteración", i+1)
            return None

        x_new = x - f(x) / dfx

        print(f"Iteración {i+1}: x = {x_new}, f(x) = {f(x_new)}")

        if abs(x_new - x) < tol:
            print("\nRaíz encontrada con la tolerancia deseada.")
            return x_new

        x = x_new

    print("\nNo se alcanzó la convergencia después del número máximo de iteraciones.")
    return None


# Ejemplo de uso:
if __name__ == "__main__":
    def f(x):
        return x**3 - x - 2  # Cambiar la función si es necesario

    def df(x):
        return 3*x**2 - 1  # Derivada de la función

    x0 = 1.5  # Valor inicial
    tol = 1e-6
    max_iter = 100

    raiz = newton_raphson(f, df, x0, tol, max_iter)

    if raiz is not None:
        print(f"\nRaíz aproximada: {raiz}")
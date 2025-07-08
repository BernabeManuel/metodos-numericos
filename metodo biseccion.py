import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define aquí la función cuya raíz quieres encontrar
    return x**3 - x - 2

def biseccion(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no se puede aplicar, f(a) y f(b) deben tener signos opuestos.")
        return None, []

    iteraciones = []
    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, iteraciones
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, iteraciones

def graficar_biseccion(f, a, b, iteraciones):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', lw=0.5)

    for i, c in enumerate(iteraciones):
        plt.plot(c, f(c), 'ro')
        plt.text(c, f(c), f'{i}', fontsize=8, color='red')

    plt.title('Método de Bisección')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    a = 1
    b = 2
    raiz, iteraciones = biseccion(f, a, b, tol=1e-5)
    if raiz is not None:
        print(f'Raíz aproximada: {raiz}')
        graficar_biseccion(f, a, b, iteraciones)
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define aquí la función
    return x**3 - x - 2

def df(x):
    # Derivada de la función
    return 3*x**2 - 1

def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    iteraciones = [x0]
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivada cero. No se puede continuar.")
            break
        x_new = x - fx/dfx
        iteraciones.append(x_new)
        if abs(x_new - x) < tol:
            return x_new, iteraciones
        x = x_new
    return x, iteraciones

def graficar_newton(f, iteraciones):
    x_vals = np.linspace(min(iteraciones)-1, max(iteraciones)+1, 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', lw=0.5)

    for i, x in enumerate(iteraciones):
        plt.plot(x, f(x), 'ro')
        plt.text(x, f(x), f'{i}', fontsize=8, color='red')

    plt.title('Método de Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x0 = 1.5  # Punto inicial
    raiz, iteraciones = newton_raphson(f, df, x0, tol=1e-5)
    print(f'Raíz aproximada: {raiz}')
    graficar_newton(f, iteraciones)
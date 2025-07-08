import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    # Define aquí la función cuya raíz quieres encontrar
    return x**3 - x - 2

def derivada(x):
    # Derivada de la función definida arriba
    return 3*x**2 - 1

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar una raíz de f.

    Parámetros:
    - f: función
    - df: derivada de la función
    - x0: aproximación inicial
    - tol: tolerancia para la convergencia
    - max_iter: máximo número de iteraciones

    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - aproximaciones: lista con todas las aproximaciones para graficar
    """
    aproximaciones = [x0]
    x = x0

    for i in range(max_iter):
        f_x = f(x)
        df_x = df(x)
        if df_x == 0:
            print(f"Derivada cero en iteración {i}, no se puede continuar.")
            break

        x_new = x - f_x / df_x
        aproximaciones.append(x_new)

        if abs(x_new - x) < tol:
            return x_new, i+1, aproximaciones

        x = x_new

    print("No se alcanzó la tolerancia en el máximo de iteraciones")
    return x, max_iter, aproximaciones

# Parámetros iniciales
x0 = 1.5
tolerancia = 1e-6
max_iteraciones = 50

# Ejecutar método
raiz, iteraciones, aproximaciones = newton_raphson(funcion, derivada, x0, tol=tolerancia, max_iter=max_iteraciones)

print(f"Raíz aproximada: {raiz}")
print(f"Iteraciones: {iteraciones}")

# Graficar función y aproximaciones
x_vals = np.linspace(min(aproximaciones)-1, max(aproximaciones)+1, 400)
y_vals = funcion(x_vals)

plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)

# Graficar puntos de aproximación
for i, aprox in enumerate(aproximaciones):
    plt.plot(aprox, funcion(aprox), 'ro')
    plt.text(aprox, funcion(aprox), f'  x{i}', fontsize=9, color='red')

plt.title("Método de Newton-Raphson - Aproximación a la raíz")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

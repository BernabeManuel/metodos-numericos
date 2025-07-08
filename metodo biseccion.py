import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    # Define aquí la función cuya raíz quieres encontrar
    return x**3 - x - 2

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de bisección para encontrar una raíz de f en [a, b]

    Parámetros:
    - f: función
    - a, b: intervalo inicial, debe cumplir f(a)*f(b)<0
    - tol: tolerancia
    - max_iter: máximo de iteraciones

    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - aproximaciones: lista con los puntos medios de cada iteración para graficar
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    aproximaciones = []
    for i in range(max_iter):
        c = (a + b) / 2
        aproximaciones.append(c)

        if abs(f(c)) < tol or (b - a)/2 < tol:
            return c, i+1, aproximaciones

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("No se alcanzó la tolerancia en el máximo de iteraciones")
    return c, max_iter, aproximaciones

# Parámetros iniciales
a = 1
b = 2
tolerancia = 1e-6
max_iteraciones = 50

# Ejecutar método
raiz, iteraciones, aproximaciones = biseccion(funcion, a, b, tol=tolerancia, max_iter=max_iteraciones)

print(f"Raíz aproximada: {raiz}")
print(f"Iteraciones: {iteraciones}")

# Graficar función y aproximaciones
x_vals = np.linspace(a-1, b+1, 400)
y_vals = funcion(x_vals)

plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)

# Graficar puntos medios de cada iteración
for i, punto in enumerate(aproximaciones):
    plt.plot(punto, funcion(punto), 'ro')
    plt.text(punto, funcion(punto), f'  c{i}', fontsize=9, color='red')

plt.title("Método de Bisección - Aproximación a la raíz")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

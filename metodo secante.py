import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    # Define aquí la función de la cual queremos encontrar la raíz
    return x**3 - x - 2

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método de la secante para encontrar una raíz de f.

    Parámetros:
    - f: función para la que se busca la raíz
    - x0, x1: aproximaciones iniciales
    - tol: tolerancia para el error
    - max_iter: número máximo de iteraciones permitidas

    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - aproximaciones: lista con todas las aproximaciones para graficar
    """
    aproximaciones = [x0, x1]

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Error: división entre cero en la iteración", i)
            break

        # Fórmula del método de la secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        aproximaciones.append(x2)

        # Verificamos si la diferencia entre aproximaciones es menor a la tolerancia
        if abs(x2 - x1) < tol:
            return x2, i+1, aproximaciones

        # Actualizamos variables para la siguiente iteración
        x0, x1 = x1, x2

    print("No se alcanzó la tolerancia deseada en el número máximo de iteraciones")
    return x2, max_iter, aproximaciones

# Parámetros iniciales
x0 = 1
x1 = 2
tolerancia = 1e-6
max_iteraciones = 50

# Ejecutar método
raiz, iteraciones, aproximaciones = secante(funcion, x0, x1, tol=tolerancia, max_iter=max_iteraciones)

print(f"Raíz aproximada: {raiz}")
print(f"Iteraciones: {iteraciones}")

# Graficar la función y las aproximaciones
x_vals = np.linspace(min(aproximaciones)-1, max(aproximaciones)+1, 400)
y_vals = funcion(x_vals)

plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label="f(x)", color="blue")
plt.axhline(0, color='black', linewidth=0.5)  # línea y=0

# Graficar puntos de aproximación en la gráfica de f(x)
for i, aprox in enumerate(aproximaciones):
    plt.plot(aprox, funcion(aprox), 'ro')  # punto rojo
    plt.text(aprox, funcion(aprox), f"  x{i}", fontsize=9, color='red')

plt.title("Método de la Secante - Aproximación a la raíz")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

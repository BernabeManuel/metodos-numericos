import numpy as np
import matplotlib.pyplot as plt


class Matriz:
    def __init__(self, filas, columnas, elementos=None):
        """Inicializa una matriz con valores dados o ceros."""
        if elementos:
            self.matriz = np.array(elementos).reshape(filas, columnas)
        else:
            self.matriz = np.zeros((filas, columnas))

    def __str__(self):
        return str(self.matriz)

    def mostrar(self, titulo="Matriz"):
        """Imprime la matriz con un título opcional."""
        print(f"\n{titulo}:\n{self.matriz}")

    def graficar(self, titulo="Matriz", cmap='viridis'):
        """Grafica la matriz como mapa de calor."""
        plt.imshow(self.matriz, cmap=cmap, interpolation='nearest')
        plt.colorbar()
        plt.title(titulo)
        plt.show()

    def suma(self, otra):
        """Suma dos matrices."""
        return Matriz(*self.matriz.shape, elementos=np.add(self.matriz, otra.matriz))

    def resta(self, otra):
        """Resta dos matrices."""
        return Matriz(*self.matriz.shape, elementos=np.subtract(self.matriz, otra.matriz))

    def multiplicacion(self, otra):
        """Multiplica dos matrices si es posible."""
        try:
            resultado = np.matmul(self.matriz, otra.matriz)
            return Matriz(resultado.shape[0], resultado.shape[1], elementos=resultado)
        except ValueError as e:
            print(f"Error en multiplicación: {e}")
            return None

    def transpuesta(self):
        """Devuelve la transpuesta de la matriz."""
        return Matriz(*self.matriz.T.shape, elementos=self.matriz.T)

    def determinante(self):
        """Calcula el determinante (solo para matrices cuadradas)."""
        if self.es_cuadrada():
            return np.linalg.det(self.matriz)
        else:
            print("Determinante solo definido para matrices cuadradas.")
            return None

    def inversa(self):
        """Devuelve la inversa si existe."""
        if not self.es_cuadrada():
            print("Solo las matrices cuadradas pueden ser invertibles.")
            return None
        try:
            inv = np.linalg.inv(self.matriz)
            return Matriz(*inv.shape, elementos=inv)
        except np.linalg.LinAlgError:
            print("La matriz no es invertible.")
            return None

    def traza(self):
        """Devuelve la traza de la matriz (suma de los elementos diagonales)."""
        if self.es_cuadrada():
            return np.trace(self.matriz)
        else:
            print("Traza solo definida para matrices cuadradas.")
            return None

    def rango(self):
        """Devuelve el rango de la matriz."""
        return np.linalg.matrix_rank(self.matriz)

    def es_cuadrada(self):
        """Verifica si la matriz es cuadrada."""
        return self.matriz.shape[0] == self.matriz.shape[1]

    def potencia(self, n):
        """Eleva la matriz a una potencia entera positiva."""
        if not self.es_cuadrada():
            print("Solo se pueden elevar al exponente matrices cuadradas.")
            return None
        try:
            resultado = np.linalg.matrix_power(self.matriz, n)
            return Matriz(*resultado.shape, elementos=resultado)
        except np.linalg.LinAlgError:
            print("No se pudo calcular la potencia de la matriz.")
            return None


# === Menú interactivo ===
def menu():
    print("=== Calculadora de Matrices ===\n")
    A = B = None

    while True:
        print("\nOpciones:")
        print("1. Crear dos matrices")
        print("2. Sumar matrices")
        print("3. Restar matrices")
        print("4. Multiplicar matrices")
        print("5. Mostrar transpuesta")
        print("6. Determinante")
        print("7. Inversa")
        print("8. Traza")
        print("9. Rango")
        print("10. Potencia de una matriz")
        print("11. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "11":
            print("Saliendo...")
            break

        elif opcion == "1":
            filas = int(input("Filas: "))
            columnas = int(input("Columnas: "))
            print(f"\nIngrese los {filas * columnas} elementos de la Matriz A:")
            elem_a = list(map(float, input().split()))
            A = Matriz(filas, columnas, elem_a)
            A.mostrar("Matriz A")
            A.graficar("Matriz A")

            print(f"\nIngrese los {filas * columnas} elementos de la Matriz B:")
            elem_b = list(map(float, input().split()))
            B = Matriz(filas, columnas, elem_b)
            B.mostrar("Matriz B")
            B.graficar("Matriz B")

        elif A is None or B is None:
            print("Primero debes crear las matrices A y B.")

        elif opcion == "2":
            C = A.suma(B)
            C.mostrar("A + B")
            C.graficar("A + B")

        elif opcion == "3":
            D = A.resta(B)
            D.mostrar("A - B")
            D.graficar("A - B")

        elif opcion == "4":
            E = A.multiplicacion(B)
            if E:
                E.mostrar("A * B")
                E.graficar("A * B")

        elif opcion == "5":
            T = A.transpuesta()
            T.mostrar("Transpuesta de A")
            T.graficar("Transpuesta de A")

        elif opcion == "6":
            det = A.determinante()
            if det is not None:
                print(f"Determinante de A: {det:.4f}")

        elif opcion == "7":
            inv = A.inversa()
            if inv:
                inv.mostrar("Inversa de A")
                inv.graficar("Inversa de A")

        elif opcion == "8":
            traza = A.traza()
            if traza is not None:
                print(f"Traza de A: {traza}")

        elif opcion == "9":
            print(f"Rango de A: {A.rango()}")

        elif opcion == "10":
            n = int(input("Exponente (entero >= 0): "))
            potencia = A.potencia(n)
            if potencia:
                potencia.mostrar(f"A^{n}")
                potencia.graficar(f"A^{n}")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
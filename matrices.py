import numpy as np
import matplotlib.pyplot as plt


class Matriz:
    def __init__(self, filas, columnas, elementos=None):
        if elementos:
            self.matriz = np.array(elementos).reshape(filas, columnas)
        else:
            self.matriz = np.zeros((filas, columnas))

    def __str__(self):
        return str(self.matriz)

    def mostrar(self, titulo="Matriz"):
        print(f"\n{titulo}:\n{self.matriz}")

    def graficar(self, titulo="Matriz", cmap='viridis'):
        plt.imshow(self.matriz, cmap=cmap, interpolation='nearest')
        plt.colorbar()
        plt.title(titulo)
        plt.show()

    def suma(self, otra):
        return Matriz(*self.matriz.shape, elementos=np.add(self.matriz, otra.matriz))

    def resta(self, otra):
        return Matriz(*self.matriz.shape, elementos=np.subtract(self.matriz, otra.matriz))

    def multiplicacion(self, otra):
        try:
            resultado = np.matmul(self.matriz, otra.matriz)
            return Matriz(resultado.shape[0], resultado.shape[1], elementos=resultado)
        except ValueError as e:
            print(f"Error en multiplicación: {e}")
            return None

    def transpuesta(self):
        return Matriz(*self.matriz.T.shape, elementos=self.matriz.T)

    def determinante(self):
        if self.matriz.shape[0] == self.matriz.shape[1]:
            return np.linalg.det(self.matriz)
        else:
            print("Determinante solo definido para matrices cuadradas.")
            return None

    def inversa(self):
        try:
            inv = np.linalg.inv(self.matriz)
            return Matriz(*inv.shape, elementos=inv)
        except np.linalg.LinAlgError:
            print("La matriz no es invertible.")
            return None


# === Menú simple ===
def menu():
    print("=== Calculadora de Matrices ===\n")
    while True:
        print("\nOpciones:")
        print("1. Crear dos matrices")
        print("2. Sumar matrices")
        print("3. Restar matrices")
        print("4. Multiplicar matrices")
        print("5. Mostrar transpuesta")
        print("6. Determinante")
        print("7. Inversa")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "8":
            break

        elif opcion == "1":
            filas = int(input("Filas: "))
            columnas = int(input("Columnas: "))
            print(f"\nIngrese los {filas * columnas} elementos de la Matriz A (separados por espacio):")
            elem_a = list(map(float, input().split()))
            A = Matriz(filas, columnas, elem_a)
            A.mostrar("Matriz A")
            A.graficar("Matriz A")

            print(f"\nIngrese los {filas * columnas} elementos de la Matriz B:")
            elem_b = list(map(float, input().split()))
            B = Matriz(filas, columnas, elem_b)
            B.mostrar("Matriz B")
            B.graficar("Matriz B")

        elif not 'A' in locals() or not 'B' in locals():
            print("Primero debes crear las matrices.")

        elif opcion == "2":
            C = A.suma(B)
            C.mostrar("Suma A + B")
            C.graficar("Suma A + B")

        elif opcion == "3":
            D = A.resta(B)
            D.mostrar("Resta A - B")
            D.graficar("Resta A - B")

        elif opcion == "4":
            E = A.multiplicacion(B)
            if E:
                E.mostrar("Multiplicación A * B")
                E.graficar("Multiplicación A * B")

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

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()

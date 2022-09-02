from tkinter import N


def run():

    def factoriales(n):
        """
        Calcula el factorial de "n"
        donde n es un entero & > 0
        """
        print(n)
        if n == 1:
            return 1
        return n * factoriales(n - 1)

    n = int(input('Escribe un número: '))

    print(f'El número factorial de {n} es: ' + str(factoriales(n)))
if __name__ == '__main__':
    run()

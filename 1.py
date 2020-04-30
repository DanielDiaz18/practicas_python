"""Escribir un ciclo definido para imprimir por pantalla todos los números entre 10 y 20."""


def iterador(i=10, end=20):
    print(i)
    if i < end:
        iterador(i+1, end)


if __name__ == "__main__":
    iterador()

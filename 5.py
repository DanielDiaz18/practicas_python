"""Programa que reciba una serie de números y arroja la media, moda, y la desviación estándar."""
import statistics

if __name__ == "__main__":
    lista = [5.12, -34.11, 32.43, -1.3, 7.83, -0.32]

    print("desviacion estandar:\t{}".format(statistics.stdev(lista)))
    print("media:\t{}".format(statistics.median(lista)))
    print("moda:\t{}".format(statistics.mode([-1.3, *lista])))

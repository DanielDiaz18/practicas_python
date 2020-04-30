"""Programa que reciba 10 números y los ordene de mayor a menor."""


def insertionSort(lista):
    for i in range(1, len(lista)):
        value = lista[i]
        j = i-1
        while value > lista[j] and j >= 0:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = value

    return lista


if __name__ == "__main__":
    lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
    print("Lista ordenada:", insertionSort(lista), "\n")

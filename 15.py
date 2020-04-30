"""Recibir 10 números e imprimir solamente los primos"""


def isPrime(n, i=2):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True

    return isPrime(n, i + 1)


def printPrimes(arr, i=0):
    if i < len(arr):
        if isPrime(arr[i]):
            print(arr[i])
        printPrimes(arr, i+1)


if __name__ == "__main__":
    lista = [12, 2, 33, 27, 64, 3, 5, 3, 9]
    # print(",".join(str(x) for x in lista if isPrime(x)))
    printPrimes(lista)

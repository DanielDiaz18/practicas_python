
"""Programa que sume todas las letras consonantes en una palabra, ejemplo Hola arroja 2."""

if __name__ == "__main__":
    cadena = "Hola"
    vocales = "aeiou"
    res = len(cadena) - len([i for i in cadena for j in vocales if j == i])

    # for i in cadena:
    #     for j in vocales:
    #         if j == i:
    #             res -= 1
    #             break

    print(res)

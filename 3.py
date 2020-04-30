"""Programa que quita todas las vocales de una palabra, ejemplo le das Hola y arroja hl."""

if __name__ == "__main__":
    cadena = ["hola", "adios", "dffsdfsd", ]
    vocales = "aeiou"
    res = "".join(i for i in cadena for x in i for j in vocales if j ==
                  x or x == j.upper())

    # for i in cadena:
    #     for j in vocales:
    #         if j == i:
    #             res = res + i
    #             break

    print(res)

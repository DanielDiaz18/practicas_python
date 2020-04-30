"""Programa que reciba una palabra y la guarde en un archivo."""

if __name__ == '__main__':
    file = open("hola.txt", "a+")
    file.write(input("ingrese el texto a guardar: "))
    file.close()

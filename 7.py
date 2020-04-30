"""Programa que reciba una palabra y el nombre del archivo donde se va a guardar"""

if __name__ == '__main__':
    file = open("{}.txt".format(input("ingrese nombre del archivo: ")), "a+")
    file.write(input("ingrese el texto a guardar: "))
    file.close()

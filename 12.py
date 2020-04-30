"""Dar un número de horas y una tarifa por hora,
luego dar un número de días y arrojar el total de dinero ganado,
considerar cada día de 8 horas laborables."""

if __name__ == "__main__":
    nHoras = int(input("ingrese un numero de horas: "))
    tarifa = float(input("ingrese la tarifa por hora: "))
    nDias = int(input("ingrese un numero de dias: "))

    print("total de dinero ganado: {}".format(min(nHoras, 8) * tarifa * nDias))

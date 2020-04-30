"""Programa que reciba un número flotante entre el 1.0 y el 10.0 y que los ordene,
    imprimiendo con letra el número más grande (solamente la parte entera),
    ejemplo el número más grande fue 9.2 arrojar Nueve."""

if __name__ == "__main__":
    nombres = (
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho ",
        "nueve",
        "diez",
    )

    while True:
        decimal = float(input("introduzca un flotante: "))
        if 1 <= decimal <= 10:
            break
        else:
            print("numero invalido")

    print(nombres[int(decimal)-1])

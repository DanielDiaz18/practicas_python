"""Programa qué pregunte el nombre de la mamá de Goku y que lo siga preguntando hasta que le atines."""


def isGokusMom():
    if input("¿Como se llama la mama de goku?:").lower() == "gine":
        print("correcto")
    else:
        print("nombre incorrecto, vuelve a intentar")
        isGokusMom()


if __name__ == "__main__":
    isGokusMom()


import Practica3_data

if __name__ == "__main__":
    contador_intentos = 0
    while contador_intentos < 3:
        usuario = str(input("Ingrese su nombre de usuario: ").lower())
        if usuario in Practica3_data.USUARIO:
            pin = int(input("Ingrese su PIN: "))
            if pin == Practica3_data.PINES[usuario]:
                print("\033[32mAcceso concedido.\033[0m")
                Practica3_data.logica_retiros(usuario)
            else:
                print(f"\033[31m PIN incorrecto. Intentos restantes: {2 - contador_intentos}\033[0m")
                contador_intentos += 1
        else:
            print(f"\033[31m No se reconoce el nombre de usuario\033[0m")
    print("\033[31mSe han agotado los intentos. Acceso denegado.\033[0m")
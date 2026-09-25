
import Practica3_data

if __name__ == "__main__":
    contador_intentos = 0
    while True:
        respuesta_activo = input("¿Desea continuar? (s/n): ").lower()
        if respuesta_activo == "n":
            print("\033[32mGracias por usar el sistema. ¡Hasta luego!\033[0m")
            break
        elif respuesta_activo != "s" and respuesta_activo != "y":
            print("\033[31mRespuesta no válida. Por favor, ingrese 's' o 'n'.\033[0m")
            continue
        usuario = str(input("Ingrese su nombre de usuario: ").lower())
        if usuario in Practica3_data.USUARIO:
            while contador_intentos < 3:
                pin = int(input("Ingrese su PIN: "))
                if pin == Practica3_data.PINES[usuario]:
                    print("\033[32mAcceso concedido.\033[0m")
                    Practica3_data.logica_retiros(usuario)
                    break
                else:
                    print(f"\033[31m PIN incorrecto. Intentos restantes: {2 - contador_intentos}\033[0m")
                    contador_intentos += 1
            else:
                print("\033[31mSe han agotado los intentos. Acceso denegado.\033[0m")
                break
        else:
            print(f"\033[31m No se reconoce el nombre de usuario\033[0m")
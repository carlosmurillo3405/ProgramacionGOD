# Datos de consulta
USUARIO = {
    "juan_el_camas": {"nombre": "Juan Guarnizo xD"},
    "diosito_es_grande_lol": {"nombre": "Maria Citlali Ximena de los Angeles Smith"},
    "xXgatita777Xx": {"nombre": "Cesar Alejandro Gonzalez Estrada"},
}

PINES = {
    "juan_el_camas": 2004,
    "diosito_es_grande_lol": 3333,
    "xXgatita777Xx": 7777,
}

# Lógica de retiros
def logica_retiros(usr):
    saldo, sumatoria_dia = 10000, 1000
    retiro, op = 0, 0
    print(f"Bienvenido {USUARIO[usr]['nombre']}, su saldo es: \033[32m${saldo}\033[0m")
    print(f"Usted ha retirado \033[32m${sumatoria_dia}\033[0m el día de hoy.")
    retiro = float(input("¿Cuánto desea retirar?: "))

    sumatoria_dia += retiro

    if retiro % 50 != 0:
        print("\033[31mMONTO NO VÁlIDO, DEBE SER MÚLTIPLO DE 50\033[0m")
    elif retiro > saldo:
        print("\033[31mSALDO INSUFICIENTE\033[0m")
    elif sumatoria_dia >= 6000:
        print("\033[31mLÍMITE DE RETIRO DIARIO ALCANZADO\033[0m")
    else:
        saldo -= retiro
        print(f"Su nuevo saldo es: \033[32m${saldo}\033[0m")
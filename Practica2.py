saldo, sumatoria_dia = 10000, 1000
retiro, op = 0, 0

print(f"Bienvenido, su saldo es: \033[32m${saldo}\033[0m")
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
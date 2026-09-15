temp, frec, sat = 0, 0, 0
temp, frec, sat = map(int, input("Introduce la temperatura, frecuencia y saturación (separadas por comas): ").split(","))
if sat < 90 or frec > 120:
    print("\033[31mROJO\033[0m")
elif temp >= 39:
    print("\033[33mAMARILLO\033[0m")
else:
    print("\033[32mVERDE\033[0m")

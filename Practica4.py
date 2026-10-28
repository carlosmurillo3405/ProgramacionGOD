import time

def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i +1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

if __name__ == "__main__":
    operacion1 = time.perf_counter()
    print(f"Tiempo de operacion: {operacion1}")
    
    lista1 = [1,2,3,4,5,6,7,8,9,0]
    objetivo = 9
    resultado = suma_objetivo(lista1, objetivo)

    operacion2 = time.perf_counter()
    print(f"Tiempo de operacion: {operacion2}")

    diferencia_tiempo = operacion2 - operacion1
    print(f"Diferencia de tiempo: {diferencia_tiempo:.6f}")
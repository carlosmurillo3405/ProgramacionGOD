import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode = 'r', newline = '', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def export_csv(data, file_path, filename):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def insertion_sort(data, llave):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j][llave] > key[llave]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

if __name__ == "__main__":
    file_path = '/home/walterms/Documents/Programación/ProgramacionGOD/Practica5/pacientes_mini.csv'
    file_path2 = '/home/walterms/Documents/Programación/ProgramacionGOD/Practica5/pacientes.csv'
    data = read_csv(file_path)
    data2 = read_csv(file_path2)

    insertion_sort(data, 0)
    insertion_sort(data2, 0)

    export_csv(data, '/home/walterms/Documents/Programación/ProgramacionGOD/Practica5/pacientes_mini_ordenado.csv', 'pacientes_mini_ordenado.csv')
    export_csv(data2, '/home/walterms/Documents/Programación/ProgramacionGOD/Practica5/pacientes_ordenado.csv', 'pacientes_ordenado.csv')

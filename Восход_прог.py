import random
from collections import Counter

matrix = []
result = []

def enter_matrix(matrix):
    matrix = input_matrix()
    if matrix:
        print("Изначальная матрица:")
        print_matrix(matrix)

    return matrix

def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = int(input(f"Введите элемент [{i}][{j}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")
        matrix.append(row)
    return matrix

def enter_rand_matrix(matrix):
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            matrix = generate_random_matrix(rows, cols)
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")
    if matrix:
        print("Изначальная матрица:")
        print_matrix(matrix)

    return matrix

def generate_random_matrix(rows, cols):
    try:
        a = int(input(f"Введите нижнюю границу эллементов: "))
        b = int(input(f"Введите верхнюю границу эллементов: "))
        matrix = [[random.randint(a, b) for _ in range(cols)] for _ in range(rows)]
        # Генерирует случайную матрицу, используя списковое включение (list comprehension).
        # Внешний список - это строки матрицы, его создаем range(rows) раз.
        # Внутренний список - это элементы в строке (столбцы), его создаем range(cols) раз.
        return matrix
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")
        return None

def process_matrix(matrixx):
    flat_matrix = [element for row in matrix for element in row]
    # Создает одномерный список (flat_matrix), объединяя все элементы матрицы в один список.

    element_counts = Counter(flat_matrix)
    # Использует Counter для подсчета частоты каждого элемента в списке flattened_matrix.

    result_matrix = [[element_counts[element] for element in row] for row in matrix]
    # Создает новую матрицу (result_matrix), где каждый элемент равен частоте появления соответствующего элемента
    # из исходной матрицы в списке element_counts.
    return result_matrix


def make_matr(matrix):
    global result
    if matrix:
        result = process_matrix(matrix)
        print("Алгоритм выполнен.")

    else:
        print("Сначала введите или сгенерируйте матрицу.")

    return result

def res(matrix, result):
    if result:
        print_matrix(matrix)
        print("Результат:")

        print_matrix(result)
    else:
        print("Сначала выполните алгоритм.")

    return matrix, result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    enter_matrix(matrix)
    matrix=enter_rand_matrix(matrix)
    result=make_matr(matrix)
    res(matrix, result)
    print_matrix(matrix)


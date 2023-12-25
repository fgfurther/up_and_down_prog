import random
from collections import Counter
import os, psutil

def input_matrix():
    while True:
        try:
            rows, cols = map(int, input("Введите количество строк и столбцов матрицы (через пробел): ").split())
            return [list(map(int, input(f"Введите элементы строки {i} через пробел: ").split()[:cols])) for i in range(rows)]

        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")




def generate_random_matrix():
    try:
        rows, cols = map(int, input("Введите количество строк и столбцов матрицы (через пробел): ").split())
        a, b = map(int, input("Введите нижнюю и верхнюю границы элементов (через пробел): ").split())
        return [[random.randint(a, b) for _ in range(cols)] for _ in range(rows)]
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")



def process_matrix(matrix):
    flat_matrix = [element for row in matrix for element in row]
    element_counts = Counter(flat_matrix)
    return [[element_counts[element] for element in row] for row in matrix]


def make_matrix(matrix):
    return process_matrix(matrix) if matrix else None


def display_result(matrix, result):
    if result:
        print_matrix(matrix)
        print("Результат:")
        print_matrix(result)
    else:
        print("Сначала выполните алгоритм.")


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    matrix = None
    while True:
        print("\nМеню:")
        print("1. Ввести матрицу")
        print("2. Сгенерировать случайную матрицу")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат (матрицу)")
        print("5. Завершить работу")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            matrix = input_matrix()

        elif choice == '2':
            matrix = generate_random_matrix()
            process = psutil.Process()
            print(process.memory_info().rss)

        elif choice == '3':
            result = make_matrix(matrix)
            if result:
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите или сгенерируйте матрицу.")

        elif choice == '4':
            display_result(matrix, make_matrix(matrix))

        elif choice == '5':
            print("Завершение работы программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий пункт меню.")
            input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
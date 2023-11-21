import random
from collections import Counter

class MatrixProcessor:
    def __init__(self):
        self.matrix = None
        self.result = None

    def input_matrix(self):
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
        self.matrix = matrix

    def generate_random_matrix(self, rows, cols, a, b):
        try:
            matrix = [[random.randint(a, b) for _ in range(cols)] for _ in range(rows)]
            return matrix
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")
            return None

    def enter_rand_matrix(self):
        while True:
            try:
                rows = int(input("Введите количество строк: "))
                cols = int(input("Введите количество столбцов: "))
                a = int(input(f"Введите нижнюю границу эллементов: "))
                b = int(input(f"Введите верхнюю границу эллементов: "))
                self.matrix = self.generate_random_matrix(rows, cols, a, b)
                break
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите целочисленные значения.")

        if self.matrix:
            print("Изначальная матрица:")
            self.print_matrix(self.matrix)

    def process_matrix(self):
        flat_matrix = [element for row in self.matrix for element in row]
        element_counts = Counter(flat_matrix)
        result_matrix = [[element_counts[element] for element in row] for row in self.matrix]
        self.result = result_matrix

    def make_matr(self):
        if self.matrix:
            self.process_matrix()
            print("Алгоритм выполнен.")
        else:
            print("Сначала введите или сгенерируйте матрицу.")

    def res(self):
        if self.result:
            self.print_matrix(self.matrix)
            print("Результат:")
            self.print_matrix(self.result)
        else:
            print("Сначала выполните алгоритм.")

    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

def print_menu():
    print("\nМеню:")
    print("1. Ввести матрицу")
    print("2. Сгенерировать случайную матрицу")
    print("3. Выполнить алгоритм")
    print("4. Вывести результат (матрицу)")
    print("5. Завершить работу")

def main():
    processor = MatrixProcessor()

    while True:
        print_menu()

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            processor.input_matrix()
            processor.result = None  # Сбрасываем результат при вводе новой матриц

        elif choice == '2':
            processor.enter_rand_matrix()
            processor.result = None  # Сбрасываем результат при вводе новой матрицы

        elif choice == '3':
            processor.make_matr()

        elif choice == '4':
            processor.res()

        elif choice == '5':
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий пункт меню.")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()

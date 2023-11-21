

class MatrixProcessor:
    def __init__(self):
        self.matrix = None
        self.result = None

    def input_matrix(self):
        pass

    def enter_rand_matrix(self):
        pass

    def generate_random_matrix(self, rows, cols, a, b):
        pass

    def process_matrix(self):
        pass

    def make_matr(self):
        pass

    def print_matrix(self, matrix):
        pass

    def res(self):
        pass

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

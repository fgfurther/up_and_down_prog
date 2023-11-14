def menu():
    print("\nМеню:")
    print("1. Ввести матрицу")
    print("2. Сгенерировать случайную матрицу")
    print("3. Выполнить алгоритм")
    print("4. Вывести результат (матрицу)")
    print("5. Завершить работу")

def main():
    while True:
        menu()

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            enter_matrix(matrix)
            result = None  # Сбрасываем результат при вводе новой матриц

        elif choice == '2':
            enter_rand_matrix(matrix)
            result = None  # Сбрасываем результат при вводе новой матрицы

        elif choice == '3':
            make_matr(matrix)

        elif choice == '4':
            res(matrix, result)

        elif choice == '5':
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий пункт меню.")
            input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
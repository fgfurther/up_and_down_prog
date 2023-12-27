import tracemalloc
from functools import reduce
import numpy as np
import struct
import sys

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year



    def __bytes__(self):
        packed_book = struct.pack('iii', self.title, self.author, self.year)
        return packed_book


class Stroka:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = str(year)
    def strokaa(self):
        return self.title + " " + self.author + " " + self.year
    def __str__(self):
        return "{}{}{}".format(self.title, self.author, self.year)


def sum_even_numbers(n):
    return sum(range(0, n, 2))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def unique_elements(lst):
    return list(set(lst))

def matrix_multiply(matrix_a, matrix_b):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)] for row in matrix_a]

def sum_even_numbers1(n):
    even_numbers = []
    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
    return sum(even_numbers)

# Пример 2: Факториал числа
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример 3: Поиск уникальных элементов в списке
def unique_elements1(lst):
    result = []
    for elem in lst:
        if elem not in result:
            result.append(elem)
    return result

# Пример 5: Умножение матриц
def matrix_multiply1(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element = 0
            for k in range(len(matrix_b)):
                element += matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        result.append(row)
    return result

def measure_memory_usage(func, *args, **kwargs):
    tracemalloc.start()
    result = func(*args, **kwargs)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Использование памяти: {current / 10**6} MB (пиковое: {peak / 10**6} MB)")
    return result

if __name__ == "__main__":
    print("1. Сумма четных чисел")
    result_1 = measure_memory_usage(sum_even_numbers, 1000000)
    result_11 = measure_memory_usage(sum_even_numbers1, 1000000)

    print("\n2. Вычисление факториала")
    result_2 = measure_memory_usage(factorial, 100000)
    result_22 = measure_memory_usage(factorial1, 100000)

    print("\n3. Уникальные элементы списка")
    result_3 = measure_memory_usage(unique_elements, range(1, 10001))
    result_33 = measure_memory_usage(unique_elements1, range(1, 10001))

    print("\n4. Запаковка и распаковка строка")
    book1 = Stroka("The Catcher in the Rye", "J.D. Salinger", 1951)
    stroka1 = measure_memory_usage(Stroka.__str__, book1)
    stroka11 = measure_memory_usage(Stroka.strokaa, book1)

    print("\n5. Запаковка и распаковка книги")
    book = Book(123, 189, 1951)
    binar_book=bytes(book)

    print(f"Использованная память: {sys.getsizeof(binar_book)}")
    print(f"Использованная память: {sys.getsizeof(book)}")

    print("\n6. Умножение матриц")
    matrix_a = np.random.randint(1000, size=(50, 50))
    matrix_b = np.random.randint(1000, size=(50, 50))
    result_5 = measure_memory_usage(matrix_multiply, matrix_a, matrix_b)
    result_55 = measure_memory_usage(matrix_multiply1, matrix_a, matrix_b)

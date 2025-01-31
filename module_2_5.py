def get_matrix(n, m, value):
    if n <= 0 or m <= 0:  # проверка на нулевые или отрицательные размеры
        return []
    matrix = []  # создаем пустой список для матрицы
    for i in range(n):  # внешний цикл для строк
        row = []  # создаем пустой список для строки
        for j in range(m):  # внутренний цикл для столбцов
            row.append(value)  # заполняем строку значениями
        matrix.append(row)  # добавляем строку в матрицу
    return matrix  # возвращаем заполненную матрицу


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

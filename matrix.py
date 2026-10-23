import numpy as np

N = int(input("Введите количество строк N:"))
M = int(input("Введите количество столбцов M:"))


def func(N,M):
    if N != M:
        print("Определитель можно найти только для квадратной матрицы (N должно быть равно M)")
        return -1   
    matrix = np.random.randint(0, 101, size=(N, M)) #заполняем матрицу от 0 до 100
    print(matrix)
    print("\n")  #исходная матрица
    tr_matrix = matrix.T   #транспонированная матрица
    print(tr_matrix)
    if N == M:
        det1 = np.linalg.det(matrix)
        print(f"Определитель исходной матрицы: {det1:.10f}")  #округление до 10 цифры после запятой
        det2 = np.linalg.det(tr_matrix)
        print(f"Определитель транспонированной матрицы: {det2:.10f}")
        if det1 == det2:
            print("Определители равны")
        elif det1 > det2:
            print("Определитель исходной матрицы больше")
        else:
            print("Определитель транспонированной матрицы больше")
    else:
        print("Ошибка: Невозможно вычислить определители, так как матрица не квадратная.")


func(N,M)

import numpy as np
from fractions import Fraction as f
def correct_fraction(s):
    s = s.split()
    row = []
    for i in s:
        if i in "tT":
            row.append("t")
        elif "f" not in i:
            row.append(int(i))
        else:
            row.append(eval(i))
    return row
def hlp():
    stroka_help = "Введите Элементы ряда через пробел, каждый ряд с новой строки;" + "\n"
    stroka_help += "После ввода матрицы введите 00 на новой строке;" + "\n"
    stroka_help += "Для ввода дроби введите её в виде: f(числитель,знамменатель)" + "\n"
    stroka_help += "Дробь ВАЖНО вводить без пробела!" + "\n"
    stroka_help += "f(a, b) - неверно, f(a,b) - верно" + "\n"
    stroka_help += "Введите матрицу:" + "\n"
    return stroka_help


def input_matrix_bt(s):
    lst = []
    s = s.split('\n')
    for i in s:
        lst.append(correct_fraction(i))
    return np.array(lst)


print(input_matrix_bt("1 2 3\n3 2 1\n2 f(4,3) 2"))

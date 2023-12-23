import numpy as np
from fractions import Fraction as f
def correct_fraction(s):
    s = s.split()
    row = []
    for i in s:
        if i in "tT":
            row.append("t")
        elif "f" not in i and "/" not in i:
            row.append(int(i))
        elif "/" in i:
            i = i.split('/')
            row.append(eval(f'f({i[0]},{i[1]})'))
        else:
            row.append(eval(i))
    return row
def hlp():
    stroka_help = "Введите элементы ряда через пробел, каждый ряд с новой строки" + "\n"
    stroka_help += "Для ввода дроби введите её в виде: 1/3" + "\n"
    return stroka_help


def input_matrix_bt(s):
    lst = []
    s = s.split('\n')
    for i in s:
        lst.append(correct_fraction(i))
    # return np.array(lst)
    return lst



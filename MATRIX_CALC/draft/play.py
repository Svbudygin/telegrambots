from MATRIX_CALC.input_matrix import hlp
from RREF import rref
from REF import ref
from oop_mat_class import Matrix
from work_with_fractions import correct_fraction
from fractions import Fraction as f
from elementary_row_operations import start_opertions

def input_matrix():
    lst = []
    print(
        "---Введите матрицу или help:---")
    s = input()
    if s.lower().strip() == "help":
        print(hlp())
    while s != "00":
        if s.lower().strip() != 'help':
            lst.append(correct_fraction(s))
        s = input()
    return lst

def start_opertions(m):
    stroka = ""
    print("Введите операцию в виде 1 2 3 (для l), 1 2 (для d), 1 2 t (для t)\nДля окончания программы введите 00")
    stroka += "Введите операцию в виде 1 2 3 (для l), 1 2 (для d), 1 2 t (для t)"
    while True:

        s = input("введите операцию (d,l,t) -->  ")
        if s == "00":
            break
        if len(s.split()) >= 4 and "f" in s or "/" in s:
            print("введите правильно дробь:\nДробь ВАЖНО вводить без пробела!\nf(a, b) - неверно, f(a,b) - верно")

        elif len(s.split()) in (1, 2, 3, 4):
            m.matrix = [*correct_fraction(s)]
            print(m.show())
def matrix_start():
    xxx = -4
    m = Matrix(input_matrix())
    inpt = input("select rref or ref or elementary_row_operations -> ").lower()
    if inpt == "rref":
        rref(m)
    elif inpt == "ref":
        print(ref(m))
    else:
        start_opertions(m)


if __name__ == "__main__":
    matrix_start()

import sqlite3

from utils.OOP import Matrix
from utils.input_matrix import input_matrix_bt, correct_fraction

stroka_ERO = (
        "Введите нужную операцию в виде:\n1 2 (для d) - умножение стоки 1 на 2\n1 2 3 (для l) - вычесть из первой строки вторую умноженную на три\n1 2 t (для t) - поменять местами первую и вторую строки" + '\n'
        + "Дроби вводить ввиде 1/3")


def start_opertions_tb(m, s):
    m = Matrix(input_matrix_bt(m))
    test = s.split()[:2]
    if len(s.split()) in (1, 2, 3, 4):
        m.matrix = [*correct_fraction(s)]
        return m.show()

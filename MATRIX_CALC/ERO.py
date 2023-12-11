import sqlite3

from input_matrix import input_matrix_bt, correct_fraction
from OOP import Matrix

stroka_ERO = ("Введите операцию в виде 1 2 3 (для l), 1 2 (для d), 1 2 t (для t)" + '\n'
              + "введите правильно дробь:\nДробь ВАЖНО вводить без пробела!\nf(a, b) - неверно, f(a,b) - верно"
              + '\n' + "введите операцию (d,l,t) -->  ")




def start_opertions_tb(m, s):
    m = Matrix(input_matrix_bt(m))

    if len(s.split()) in (1, 2, 3, 4):

        m.matrix = [*correct_fraction(s)]
        print(correct_fraction(s))
        conn = sqlite3.connect("mat.sql")
        cursor = conn.cursor()
        print(m.show_entry(), r'{m.show_entry()}', "3454345")
        cursor.execute(f'INSERT INTO mat (matrix) VALUES ("%s")' % (m.show_entry()))
        conn.commit()
        cursor.close()
        conn.close()
        return m.show()

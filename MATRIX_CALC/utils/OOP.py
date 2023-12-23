from fractions import Fraction as f
import numpy as np


class Matrix:
    def __init__(self, mat: list):
        self.__mat = mat  # двумерный массив для матрицы
        self.__n = 0  # номер матрицы

    def transposition(self):
        X = self.matrix
        self.__mat = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
        return self.__mat

    def d(self, row, mult):
        """elementary row operation d"""
        for j in range(len(self[row - 1])):
            self[row - 1][j] *= mult
        return self.matrix

    def l(self, row1, row2, mult):
        for j in range(len(self[row1 - 1])):
            self[row1 - 1][j] += mult * self[row2 - 1][j]
        return self.matrix

    def l_col(self, col1, col2, mult, *args):
        for j in range(len(self[col1 - 1])):
            self[j][col1 - 1] += mult * self[j][col2 - 1]
        return self.matrix

    def t(self, row1, row2, *args):
        self[row1 - 1], self[row2 - 1] = self[row2 - 1].copy(), self[row1 - 1].copy()

    @property
    def matrix(self):
        return self.__mat

    @matrix.setter
    def matrix(self, args):
        if len(args) == 4:
            self.l_col(*args)
        elif len(args) == 3:
            if "t" in args:
                self.t(*args)
            else:
                self.l(*args)
        elif len(args) == 2:
            self.d(*args)
        else:
            raise IndexError("для l введите три значения, для d два")

    def show(self, short=True):
        "Красивый вывод матрицы"
        stroka = ""
        mx = -float("inf")
        # arr.shape -> (3,3)
        # arr.size -> 9
        # arr.resize .reshape
        for i in range(len(self.matrix)):
            mx = max(list(map(lambda x: len(str(x)), self[i])) + [mx])
        for i in range(len(self.matrix)):
            i = map(lambda x: (" " * mx + str(x))[-mx:], self[i])
            stroka += " ".join(i) + '\n'
        return stroka.strip()

    def show_entry(self, short=True):
        "Красивый вывод матрицы"
        stroka = ""
        for i in self.matrix:
            stroka += " ".join(list(map(lambda x: str(x), i))) + '\n'
        return stroka.strip()

    def show_with_num(self, short=True):
        "Красивый вывод матрицы"
        stroka = ""
        self.__n += 1
        if short:
            stroka += f"-----------matrix {self.__n}-----------" + '\n'
        else:
            stroka += f"----------- final matrix -----------" + '\n'
        mx = -float("inf")
        for i in range(len(self.matrix)):
            mx = max(list(map(lambda x: len(str(x)), self[i])) + [mx])
        for i in range(len(self.matrix)):
            i = map(lambda x: (" " * ((mx - len(str(x))) * 2 + 1) + str(x)), self[i])

            stroka += "[" + " ".join(i) + "]" + '\n'
        return stroka

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

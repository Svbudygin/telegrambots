from fractions import Fraction as f

from  utils.input_matrix import input_matrix_bt
from  utils.OOP import Matrix


def transposition(m):
    m = input_matrix_bt(m)
    return Matrix(Matrix(m).transposition()).show()

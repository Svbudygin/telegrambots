from fractions import Fraction as f
from input_matrix import input_matrix_bt
from OOP import Matrix


def rref(m, dett=False, long=False):
    m = Matrix(input_matrix_bt(m))
    Steps = m.show_with_num()
    stairs = 0
    for col in range(len(m.matrix[0])):
        operation_oper_group = ""
        if len(m.matrix) == stairs:
            break
        if m[stairs][col] != 0:
            if f(1, m[stairs][col]) != 1:
                operation_oper_group += f"d({stairs + 1}, {f(1, m[stairs][col])})" + '\n'
            m.matrix = [stairs + 1, f(1, m[stairs][col])]
            stairs += 1
        else:
            for row in range(stairs + 1, len(m.matrix)):
                if m[row][col] != 0:
                    operation_oper_group += f"t({stairs + 1}, {row + 1})" + '\n'
                    m.matrix = [stairs + 1, row + 1, 't']
                    if f(1, m[stairs][col]) != 1:
                        operation_oper_group += f"d({stairs + 1}, {f(1, m[stairs][col])})" + '\n'
                    m.matrix = [stairs + 1, f(1, m[stairs][col])]
                    stairs += 1
                    break
            else:
                continue
        for row in range(stairs, len(m.matrix)):
            if -m[row][col] != 0:
                operation_oper_group += f"l({row + 1}, {stairs}, {-m[row][col]})" + '\n'
            m.matrix = [row + 1, stairs, -m[row][col]]
        for row in range(stairs - 1):
            if -m[row][col] != 0:
                operation_oper_group += f"l({row + 1}, {stairs}, {-m[row][col]})" + '\n'
            m.matrix = [row + 1, stairs, -m[row][col]]

        Steps += operation_oper_group + m.show_with_num()

    Rref = m.show_with_num(short=False)
    if long:
        return Steps
    return Rref

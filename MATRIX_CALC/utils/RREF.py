from fractions import Fraction as f
from  utils.input_matrix import input_matrix_bt
from  utils.OOP import Matrix


def rref(m, dett=False, long=False, inv=False):
    m = Matrix(input_matrix_bt(m))
    Steps = m.show_with_num()
    stairs = 0
    inversemt = Matrix([[0 if i != j else 1 for i in range(len(m.matrix[0]))] for j in range(len(m.matrix))])
    for col in range(len(m.matrix[0])):
        operation_oper_group = ""
        if len(m.matrix) == stairs:
            break
        if m[stairs][col] != 0:
            if f(1, m[stairs][col]) != 1:
                operation_oper_group += f"d({stairs + 1}, {f(1, m[stairs][col])})" + '\n'
            unit = m[stairs][col]
            m.matrix = [stairs + 1, f(1, m[stairs][col])]
            inversemt.matrix = [stairs + 1, f(1, unit)]
            stairs += 1
        else:
            for row in range(stairs + 1, len(m.matrix)):
                if m[row][col] != 0:
                    operation_oper_group += f"t({stairs + 1}, {row + 1})" + '\n'
                    m.matrix = [stairs + 1, row + 1, 't']
                    inversemt.matrix = [stairs + 1, row + 1, 't']
                    if f(1, m[stairs][col]) != 1:
                        operation_oper_group += f"d({stairs + 1}, {f(1, m[stairs][col])})" + '\n'
                    unit = m[stairs][col]
                    m.matrix = [stairs + 1, f(1, m[stairs][col])]
                    inversemt.matrix = [stairs + 1, f(1, unit)]
                    stairs += 1
                    break
            else:
                continue
        for row in range(stairs, len(m.matrix)):
            if -m[row][col] != 0:
                operation_oper_group += f"l({row + 1}, {stairs}, {-m[row][col]})" + '\n'
            unit = -m[row][col]
            m.matrix = [row + 1, stairs, -m[row][col]]
            inversemt.matrix = [row + 1, stairs, unit]
        for row in range(stairs - 1):
            if -m[row][col] != 0:
                operation_oper_group += f"l({row + 1}, {stairs}, {-m[row][col]})" + '\n'
            unit = -m[row][col]
            m.matrix = [row + 1, stairs, -m[row][col]]
            inversemt.matrix = [row + 1, stairs, unit]
        Steps += operation_oper_group + m.show_with_num()
    Rref = m.show_with_num(short=False)
    if inv:
        return inversemt.show()
    if long:
        return Steps
    return Rref

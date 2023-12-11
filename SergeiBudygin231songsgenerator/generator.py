from utils.mathh import simularity
from utils.picklee import get_smt_dict
from random import randint, choices


def work_with_dict(d):
    for key in d:
        d[key] = sorted(list(d.get(key).items()), key=lambda x: [x[1], len(x[0])], reverse=True)
    return d


def rand_choices(lst):
    k = sum(list(map(lambda x: x[-1], lst)))
    lst1 = list(map(lambda x: x[-1] / k, lst))
    lst2 = list(map(lambda x: x[0], lst))
    return choices(lst2, weights=lst1)


def generator_track(name, start: str, n=12):
    n = int(n)
    d = work_with_dict(get_smt_dict(name))
    s = ""
    current_word = start
    for j in range(1, n + 1):
        s += current_word + ' ' if j % 6 != 0 else current_word + ' \n'
        if current_word in d:
            current_word = rand_choices(d.get(current_word))[0]
        else:
            sim = 0
            word = current_word
            for i in d.keys():
                x = simularity(current_word, i)
                if x > sim:
                    sim = x
                    word = i
            lstt = d.get(word)
            current_word = lstt[randint(0, len(list(filter(lambda x: x[1] == lstt[0][1] - 1, lstt))))][0]
    return s


if __name__ == "__main__":
    generator_track()

from typing import List
from parsee.parse_singers_name import get_artists_list
from utils.picklee import set_smt_dict, get_smt_list, get_smt_dict

""" создаёт разово pickle files содержащие словари со словами из всех песен определённых исполнителей """


def dict_creation(listok: List[List[object]], name):
    if "/" in name:
        return None
    dict_words = {}
    for lst in listok:
        lst = list(filter(
            lambda x: (len(x) > 3 or x in 'ямытывыВ И') and x not in '8 Воу В0132456789qwertyuioplkjhgfdsxcvbnm', lst))
        for ind, word in enumerate(lst[:-1]):
            if word not in " Воу  Т  Н ":
                if word == lst[ind + 1]:
                    variable = dict_words.get(word, {})
                    dict_words[word] = variable
                else:
                    variable = dict_words.get(word, {lst[ind + 1]: 0})
                    var = variable.get(lst[ind + 1], 0)
                    variable[lst[ind + 1]] = var + 1
                    dict_words[word] = variable
    set_smt_dict(dict_words, name)
    print(name, 200)
    return dict_words




if __name__ == "__main__":
    dict_creation(get_smt_list("Basta"), "Basta")
    # for i in get_artists_list():
    #     if "/" in i:
    #         continue
    #     try:
    #         dict_creation(get_smt_list("Basta"), "Basta")
    #     except FileNotFoundError:
    #         continue


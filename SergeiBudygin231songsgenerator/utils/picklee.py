import pickle


def set_smt_list(lst: list, name: str):
    with open(f'lyrics/{name}_tracks_text.pickle', 'wb') as f:
        return pickle.dump(lst, f, pickle.HIGHEST_PROTOCOL)


def get_smt_list(name: str):
    with open(f'lyrics/{name}_tracks_text.pickle', 'rb') as f:
        return pickle.load(f)


def set_smt_dict(lst: dict, name: str):
    with open(f'dicts/{name}dict.pickle', 'wb') as f:
        return pickle.dump(lst, f, pickle.HIGHEST_PROTOCOL)


def get_smt_dict(name):
    with open(f'dicts/{name}dict.pickle', 'rb') as f:
        return pickle.load(f)

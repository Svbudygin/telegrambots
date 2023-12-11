from generator import generator_track
from work_with_lyrics import dict_creation
from utils.picklee import get_smt_list

if __name__ == "__main__":
    s = generator_track(*['basta', 'печка', 29])
    print(s)

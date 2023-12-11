def simularity(word1: str, word2: str):
    w1, w2 = [], []
    for i in range(len(word1) - 1):
        w1.append(word1[i:i + 2])
    for i in range(len(word2) - 1):
        w2.append(word2[i] + word2[i + 1])
    return len(set(word1) & set(word2)) + 5 * len(set(w1) & set(w2))

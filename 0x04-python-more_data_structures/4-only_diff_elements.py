#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diffWords = set()
    for words in set_1:
        if words not in set_2:
            diffWords.append(words)
    for words in set_2:
        if words not in set_1:
            diffWords.append(words)

    return diffWords

#!/usr/bin/python3

def best_score(a_dictionary):
    """Return a key with the biggest interger value."""
    score = None
    keys = list(a_dictionary.keys())
    scores = list(a_dictionary.values())
    score = keys[scores.index(max(scores))]
    return score

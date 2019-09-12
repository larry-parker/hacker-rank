#!/bin/python3

import math
import os
import random
import re
import sys

class Score:
    """ Stores a score as tuple t"""

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Score(self.x + other.x, self.y + other.y)

    def get_score_as_list(self):
        return [self.x, self.y]


class Person:
    def __init__(self, name: str = "", scores: list = None):
        self.name = name
        self.scores = scores



# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    p_a = Person(name="alice", scores=a)
    p_b = Person(name="bob", scores=b)

    def cmp_scores(index):
        if p_a.scores[index] > p_b.scores[index]:
            return Score(1, 0)
        if p_a.scores[index] == p_b.scores[index]:
            return Score(0, 0)
        else:
            return Score(0, 1)

    def sum_scores(score_list):
        if not score_list:
            return Score(0, 0)
        else:
            return score_list.pop() + sum_scores(score_list)

    scores = [cmp_scores(i) for i in [0, 1, 2]]

    score = sum_scores(scores)

    return score.get_score_as_list()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

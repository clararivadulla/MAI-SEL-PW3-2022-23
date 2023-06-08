import math
import os
import numpy as np
import pandas as pd
from preprocessing import travel_dataset_xls_preprocessing
import time
from math import sin, cos, pi

root = '/Users/clararivadulla/Repositories/SEL-PW3'
root = os.path.dirname(os.getcwd())
travel_dataset_xls_preprocessing(root)
S = pd.read_csv(f"{root}/data/travel.csv")

def search(S, y):

    """
    Search algorithm using flat memory.
    :param S: the set of cases in the case base
    :param y: the new case
    :return: index of the nearest case
    """

    N = S.shape[0] # Number of cases that already exist
    best_dissimilarity = np.inf
    for i in range(N):
        dissimilarity = euclidean_distance(S[i], y, np.ones(10))
        if dissimilarity <= best_dissimilarity:
            r = i
            best_dissimilarity = dissimilarity
        print(dissimilarity)
    return r

def euclidean_distance(S_i, y, weights):
    distance = 0
    for j in range(len(S_i)):
        weight = weights[j]
        if isinstance(S_i[j], (int, float)): # Continuous
            atr_dist = abs(S_i[j] - y[j])
        else: # Discrete
            if S_i[j] != y[j]:
                atr_dist = 1
            else:
                atr_dist = 0
        distance += (weight ** 2) * (atr_dist ** 2)
    return math.sqrt(distance / np.sum(weights**2))







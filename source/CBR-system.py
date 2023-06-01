import math

import numpy as np
import pandas as pd
from preprocessing import travel_dataset_xls_preprocessing

path = '/Users/clararivadulla/Repositories/SEL-PW3'
travel_dataset_xls_preprocessing(path)
S = pd.read_csv(f"{path}/data/travel.csv").to_numpy()

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

row = S[0]
row2 = S[1]
print(row)
print(row2)
print(search(S, row))
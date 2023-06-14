from Retrieve import retrieve
import os
import time
import numpy as np
import pandas as pd
from preprocessing import travel_dataset_xls_preprocessing
from Adaptation import null_adaptation, weighted_adaptation
from sklearn.model_selection import train_test_split
import Retrieve

#root = '/Users/clararivadulla/Repositories/SEL-PW3'
# root = os.path.dirname(os.getcwd())
root = os.getcwd()
travel_dataset_xls_preprocessing(root)
data_folder = f"{root}/data"
CB = pd.read_csv(f"{data_folder}/travel.csv")
train, test = train_test_split(CB, test_size=0.2, random_state=0, shuffle=True)

labels_full = ["holiday-type", "price", "num-persons", "region", "transportation", "duration", "season", "accomodation", "hotel"]
labels_test = ["num-persons", "region", "transportation", "duration", "season", "accomodation"]
test_distances_ms = [] # Most similar
test_distances_wa = [] # Weighted adaptation
for index, row in test.iterrows():
    # New case from test set
    new_case = pd.Series([row[lb] for lb in labels_test], index=labels_test)
    original_case = pd.Series([row[lb] for lb in labels_full], index=labels_full)
    # Retrieve the most similar case
    start_time = time.time()
    
    most_similar_cases, distances = retrieve(train, new_case, data_folder, 7)
    suggested_case = weighted_adaptation(new_case, train.loc[most_similar_cases])

    # print("-----")
    # print(original_case)
    # print(suggested_case)

    distances_wa = Retrieve.calculate_distance(original_case, suggested_case, Retrieve.get_attr_dict(data_folder))
    distances_ms = Retrieve.calculate_distance(original_case, train.loc[most_similar_cases[0]], Retrieve.get_attr_dict(data_folder))

    #null_adapted_case = null_adaptation(new_case, train.loc[most_similar_cases[0]])
    #weighted_adaptation_case = weighted_adaptation(new_case, train.loc[most_similar_cases])
    end_time = time.time()

    #print("------ Most similar case ------")
    #print(train.loc[most_similar_cases[0]])
    #print("----- Null adapted case -----")
    #print(null_adapted_case)
    #print("----- Weight adapted case -----")
    #print(weighted_adaptation_case)
    #print("------ ----------------- ------")
    #print("Time taken:", end_time - start_time, "seconds")
    #print("distance:", distances.iloc[0])
    test_distances_wa.append(distances_wa/3)
    test_distances_ms.append(distances_ms/3)
    #break

print("----- Weight adapted case distances -----")
print(test_distances_wa)
print("----- Most similar case distances -----")
print(test_distances_ms)

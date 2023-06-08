from Retrieve import retrieve
import os
import time
import numpy as np
import pandas as pd
from preprocessing import travel_dataset_xls_preprocessing

#root = '/Users/clararivadulla/Repositories/SEL-PW3'
root = os.path.dirname(os.getcwd())
travel_dataset_xls_preprocessing(root)
CB = pd.read_csv(f"{root}/data/travel.csv")

new_case = pd.Series([ "Bathing", 2499, 2, "Egypt", "Car", 14.0, "April", "TwoStars", "Hotel White House, Egypt"],
                     index=[ "holiday-type", "price", "num-persons", "region", "transportation", "duration", "season", "accomodation", "hotel"])
# Retrieve the most similar case
start_time = time.time()
most_similar_case, distance = retrieve(CB, new_case)
end_time = time.time()
print(CB.loc[most_similar_case])
print("Time taken:", end_time - start_time, "seconds")
print("distance:", distance)
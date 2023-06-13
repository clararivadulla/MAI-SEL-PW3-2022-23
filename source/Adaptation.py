import pandas as pd

indexes=[ "holiday-type", "price", "num-persons", "region", "transportation", "duration", "season", "accomodation", "hotel"]

def null_adaptation(new_case, most_similar_case):    
    adapted_case = []

    for index in indexes:
        if index in new_case:
            adapted_case.append(new_case[index])
        else:
            adapted_case.append(most_similar_case[index])

    return pd.Series(adapted_case, index=indexes)


def weighted_adaptation(new_case, most_similar_cases):
    change_selected_region = True
    adapted_case = []

    ### Rules
    # Filter by a given region or the most common one in the most_similar_cases
    region = most_similar_cases['region'].value_counts().idxmax()
    if 'region' in new_case and new_case['region'] is not None :
        # Validate if there are rows matching the selected region, if not keep the most common one
        if len(most_similar_cases[most_similar_cases['region'] == new_case['region']]) > 0:
            region = new_case['region']
            change_selected_region = False

    
    most_similar_cases = most_similar_cases[most_similar_cases['region'] == region]

    for index in indexes:
        if index == 'region' and change_selected_region:
            adapted_case.append(most_similar_cases[index].value_counts().idxmax())

        elif index in new_case and new_case[index] is not None :
            adapted_case.append(new_case[index])
            
        else:
            adapted_case.append(most_similar_cases[index].value_counts().idxmax())

    return pd.Series(adapted_case, index=indexes)

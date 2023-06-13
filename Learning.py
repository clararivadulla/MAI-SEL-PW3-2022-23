def add_new_case(new_case, CB):
    new_CB = CB.copy
    new_CB.loc[len(new_CB.index)] = new_case
    return new_CB

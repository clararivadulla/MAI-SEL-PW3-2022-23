def add_new_case(new_case, CB):
    CB = pd.concat([CB, new_case.to_frame().T], ignore_index=True)
    return None

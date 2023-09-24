def best_score(a_dictionary):
    if len(a_dictionary)==0:
        return None
    M = max(a_dictionary)
    for key,val in a_dictionary:
        if val == M:
            return key

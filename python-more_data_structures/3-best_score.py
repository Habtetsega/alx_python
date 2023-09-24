def best_score(a_dictionary):
    if len(a_dictionary)==0:
        return None
    M = max(a_dictionary,lambda k:a_dictionary[k])
    return M

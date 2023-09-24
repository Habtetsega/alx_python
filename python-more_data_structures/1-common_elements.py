def common_elements(set_1, set_2):
    com=[]
    for i in set_1:
        for j in set_2:
            if i==j:
                com.append(i)
    return com

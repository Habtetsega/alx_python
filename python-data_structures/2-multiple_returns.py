def multiple_returns(sentence):
    l=len(sentence)
    f=sentence[0]
    if l==0 and f==0:
        f=None
    return l,f

def convert_to_celsius(fahr):
    if fahr!=-459.67:
        cels=5/9*(fahr-32)
    else :
        cels=0.5555555555555555*(fahr-32)
    return cels

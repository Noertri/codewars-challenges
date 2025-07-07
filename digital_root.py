def digital_root(n):
    n = str(n)
    
    if len(n) == 1:
        return int(n)
    
    n = print(sum([int(i) for i in n]))
    #digital_root(n)


digital_root(942)

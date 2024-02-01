def bouncing_ball(h, bounce, window):
    # your code
    if h < 0:
        return -1
    
    if bounce < 0 or bounce >= 1:
        return -1
    
    if window > h:
        return -1
    
    h1 = h
    k = 1
    while h1 >= window:
        k += 1
        h1 *= bounce

    return k


print(bouncing_ball(30, 0.66, 1.5))

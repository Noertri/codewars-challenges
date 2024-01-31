def create_phone_number(n):
    #your code here
    if len(n) == 10:
        letter = "".join([str(i) for i in n])
        return "({0}) {1}-{2}".format(letter[:3], letter[3:6], letter[6:])
    

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

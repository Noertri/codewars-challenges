def lottery(s: str):
    digit_list = [c for c in s if c.isdigit()]
    
    if not digit_list:
        return "One more run!"
    
    digit_string = ""

    while digit_list:
        d = digit_list.pop(0)

        if d not in digit_string:
            digit_string += d

    return digit_string


print(lottery("wQ8Hy0y5m5oshQPeRCkG"))

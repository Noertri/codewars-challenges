import re

def validate_pin(pin):
    #return true or false
    pattern = re.compile(r"^\d{4}$|^\d{6}$")
    non_number = re.compile(r"([\s]+)")
    if pattern.search(pin) and not non_number.search(pin):
        return True
    else:
        return False     


ans = validate_pin("1234\n")

print(ans)
from string import ascii_lowercase


def add_letters(*letters):
    alphabet_list = [*ascii_lowercase]

    if len(letters) == 0:
        return "z"
    else:
        jml = 0

        for l in letters:
            jml += alphabet_list.index(l)+1

        if jml > len(alphabet_list):
            jml = jml % len(alphabet_list)

        return alphabet_list[jml-1]
    

print(add_letters("z", "a"))

def get_count(sentence: str):
    return sum(list(map(lambda x: sentence.count(x), ["a", "i", "u", "e", "o"])))


print(get_count("aeiou"))
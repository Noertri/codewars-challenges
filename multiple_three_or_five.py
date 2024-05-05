def solution(number):
    if number <= 0:
        return 0
    
    items = list(filter(lambda x: x if x%3 == 0 or x%5 == 0 else False, [i for i in range(number)]))

    return sum(items)


print(solution(3))

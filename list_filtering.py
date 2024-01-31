# def filter_list(l):
#     '''return a new list with the strings filtered out'''
#     result = []
#     for i in l:
#         if isinstance(i, (str,)):
#             continue
#         result.append(i)
#     return result


def filter_list(l):
    '''return a new list with the strings filtered out'''
    return list(filter(lambda x: False if isinstance(x, (str,)) else True, l))

print(filter_list([1, 'a', 'b', 0, 15]))

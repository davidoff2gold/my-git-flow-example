def flatten_list(list_before):
    list_after = []
    for item in list_before:
        if isinstance(item, list):
            list_after.extend(flatten_list(item))
        else:
            list_after.append(item)
    return list_after

# Przykładowe dane z zagnieżdżeniami
numbers = [1, [2, 3, [4, 5]], 6, [7, 8], 9]

numbers_after = flatten_list(numbers)
print(numbers_after)

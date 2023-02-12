def corresponding_pairs(arr1, arr2) -> list:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    return list(zip(arr1,arr2))


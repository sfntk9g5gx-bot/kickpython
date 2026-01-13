# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    common = set(list1) & set(list2)

    return sorted(common)
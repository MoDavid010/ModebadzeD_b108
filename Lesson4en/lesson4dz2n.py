def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
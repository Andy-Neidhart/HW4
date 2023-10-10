def merge_lists(list1, list2):
    merged_list = list1 + list2
    for i in range(1, len(merged_list)):
        key = merged_list[i]
        j = i - 1
        while j >= 0 and key < merged_list[j]:
            merged_list[j + 1] = merged_list[j]
            j -= 1
        merged_list[j + 1] = key
    return merged_list

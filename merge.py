def merge_lists(list1, list2):
    merged_list = list1 + list2
    for i in range(1, len(merged_list)):
        min_index = i
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])
    return merged_list

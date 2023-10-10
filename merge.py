def merge_list(list1, list2):
    # Check if input lists are valid
    if not all(isinstance(num, int) for num in list1) or not all(isinstance(num, int) for num in list2):
        raise TypeError("Input lists should only contain integers.")
    
    # Merge the two lists
    merged_list = list1 + list2
    
    # Perform merge sort without using built-in sort functions
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        merged = []
        left_idx, right_idx = 0, 0
        
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        return merged
    
    # Sort and return the merged list
    sorted_list = merge_sort(merged_list)
    return sorted_list

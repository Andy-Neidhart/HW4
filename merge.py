def merge_list(list1, list2):
  merged_list = list1 + list2
      for i in range(len(merged_list)):
          for j in range(i + 1, len(merged_list)):
              if merged_list[i] > merged_list[j]:
                  temp = merged_list[i]
                  merged_list[i], merged_list[j] = merged_list[j], temp
      return merged_list

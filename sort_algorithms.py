from rich import print

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(lst):
     if len(lst) <= 1:
          return lst
     mid = len(lst)//2
     left_half = lst[:mid]
     right_half = lst[mid:]

     return merge(merge_sort(left_half), merge_sort(right_half))

def merge (left, right):
    merge_list = []
    left_index = 0
    right_index = 0
     
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merge_list.append(left[left_index])
            left_index +=1
        else:
             merge_list.append(right[right_index])
             right_index +=1
        
    while left_index < len(left):
        merge_list.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merge_list.append(right[right_index])
        right_index += 1

    return merge_list

def sort_by_timsort(lst):
    return sorted(lst)


if __name__ == "__main__":
    print(merge_sort([3,1,2]))
    print(insertion_sort([3,1,2]))
    print(sort_by_timsort([3,1,2]))
          
        
     

def merge_sort(array):
    if len(array) <= 1:
        return 
    #Divide the list
    mid = len(array) // 2
    left = array[:mid] #index 0 to before mid
    right = array[mid:] #index mid to last
    merge_sort(left)
    merge_sort(right)
    return merge_sort_two_sorted_lists(left,right,array)


def merge_sort_two_sorted_lists (a,b,array):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k += 1
    #if two list have different length
    while i < len_a :   
        array[k] = a[i]
        i += 1
        k += 1
        
    while j < len_b :
        array[k] = b[j]
        j += 1
        k += 1
        
if __name__ == "__main__":
    element_list = []
    element_list1 = [1,2,3,4,5,6,7,8,9]
    element_list2 = [9,8,7,6,5,4,3,2,1]
    element_list3 = [3]
    
    merge_sort(element_list3)
    print(element_list3)
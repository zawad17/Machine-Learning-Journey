def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
            
            
if __name__ == "__main__":
    array = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [2,5,1, 5,7 ,0,8,12,56,53],
             [],
             [34]]
    for i in array:
        selection_sort(i)
        print(f"Sorted List : {i}")
def shell_sort (array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >=gap and array[j - gap] > temp:
                array[j] =array[j - gap]
                j -= gap
            array[j] = temp
        gap //=2
        
        
if __name__ == "__main__":
    array = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [2,5,1, 5,7 ,0,8,12,56,53],
             [],
             [34]]
    for i in array:
        shell_sort(i)
        print(f"Sorted List : {i}")
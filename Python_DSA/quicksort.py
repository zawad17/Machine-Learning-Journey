def swap (a, b, array):
    if a!= b :
        temp = array[a]
        array[a] = array[b]
        array[b] = temp
        
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[start]
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
                
        if start < end:
            swap(start, end, elements)
    swap(pivot_index,end,elements)    
    return end
            
            
            
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)
        
        
if __name__ == "__main__":
    array = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [2,5,1, 5,7 ,0,8,12,56,53],
             [],
             [34]]
    for i in array:
        quick_sort(i,0,len(i)-1)
        print(f"Sorted List : {i}")
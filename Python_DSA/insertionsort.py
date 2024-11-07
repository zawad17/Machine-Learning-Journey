def insertion_sort(elements):
    for i in range(1,len(elements)):
        current = elements[i]
        j = i - 1
        while j >= 0 and current < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = current
        
if __name__ == "__main__":
    array = [[2, 43, 23, 51, 4, 6, 9],
             [1,2,3,4,5,6,7,8,9],
             [],
             [12]]
    for elements in array:
        insertion_sort(elements)
        print(f"Sorted list: {elements}")
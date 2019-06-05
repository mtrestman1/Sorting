# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    new_arr = []
    
    for i in range(0, elements):
        if len(arrA) == 0:
            new_arr.append(arrB[0])
            arrB.pop(0)
            continue
        if len(arrB) == 0:
            new_arr.append(arrA[0])
            arrA.pop(0)
            continue
        
        if arrA[0] < arrB[0]:
            new_arr.append(arrA[0])
            arrA.pop(0)
        else:
            new_arr.append(arrB[0])
            arrB.pop(0) 

    return new_arr

print(merge([1, 3, 5], [2, 4]))

    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    

    return merge(left, right)




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

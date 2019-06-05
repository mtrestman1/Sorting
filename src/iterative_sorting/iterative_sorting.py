# TO-DO: Complete the selection_sort() function below 
array = [5, 4, 7, 1, 2]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x



        # TO-DO: swap
        #arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        something = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = something


    return arr
print(selection_sort(array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for x in range(0, len(arr) - 1):
            if arr[x] > arr[x + 1]:
                something = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = something
    return arr
print(bubble_sort(array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
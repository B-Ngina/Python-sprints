def sort_and_swap(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if i % 3 == 0:

            arr[i], arr[i-1] = arr[i-1],arr[i]
       
  
    return arr

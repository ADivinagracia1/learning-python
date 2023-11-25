def mergeSort(arr):
    if len(arr) > 1:
        left  = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        # Recursive step (break array down)
        mergeSort(left)
        mergeSort(right)
    
        # Merge step
        l = 0   # index in left array
        r = 0   # index in right array 
        k = 0   # merged array index
        # loop through both arrays simultaneously
        while l < len(left) and r < len(right):
            # comapre each element and insert to merged array
            if left[l] < right[r]:
                arr[k] = left[l]
                l+=1
            else:
                arr[k] = right[r]
                r += 1 
            k+=1

        # insert leftover elements of left array
        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        # insert leftover elements of right array
        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1





arr_test = [2,3,5,1,7,4,4,4,2,3452 ,3245 ,2345,234,55,324523,43,532,4523,45243,523,4]
print(arr_test)
mergeSort(arr_test) # pass by value
print(arr_test)


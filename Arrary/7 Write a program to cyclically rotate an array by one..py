#write a program to cyclically rotate an array by one

def cyclic_rotate(arr):
    temp = arr[len(arr)-1]
    for i in range(-1,-len(arr),-1):
        arr[i] = arr[i-1]
    arr[0]=temp
    return arr

arr = [1, 8, 3, 7, 3, 5, 4]
print(cyclic_rotate(arr))   
    
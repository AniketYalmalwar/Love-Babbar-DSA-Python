
def negative_moving_one_side(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j] >=0 and arr[j+1]<0:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [3,5,-2,-1,6,-3,4,2,-1]
print(negative_moving_one_side(arr))
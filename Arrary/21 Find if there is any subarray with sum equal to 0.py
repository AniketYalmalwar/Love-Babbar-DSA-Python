# Find if there is any subarray with sum equal to 0

def subarray_sum_zero(arr):
    sub_array=[]
    for i in range(len(arr)-1):
        sum = arr[i]
        for j in range(i+1,len(arr)):
            sum += arr[j]
            if sum ==0:
                sub_array.append(arr[i:j+1])
    return sub_array

arr = [1, 2, -3, 4, 4, 2, -8, 1, -1, 5, -5]
print(subarray_sum_zero(arr))
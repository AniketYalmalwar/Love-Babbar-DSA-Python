def count_inversion(arr):
    count =0
    for i in range(len(arr)-1):
        sum1 = sum(1 for element in arr[i+1:] if element < arr[i])
        count +=sum1
    return count

arr = [2, 3, 4, 5, 6]
print(count_inversion(arr))
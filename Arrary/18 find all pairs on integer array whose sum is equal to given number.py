# find all pairs on integer array whose sum is equal to given number

def array_pair(arr,k):
    count =0
    for i in range(len(arr)-1):
        sum1 = sum(1 for element in arr[i+1:] if element + arr[i]==k)
        count +=sum1
    return count
k = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array_pair(arr,k))
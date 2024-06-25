# Kadane's Algo 

def largest_sum(arr):
    max_sum =arr[0]
    for i in range(len(arr)-1):
        sum = arr[i]
        for j in range(i+1,len(arr)):
            sum +=arr[j]
            if sum >max_sum:
                max_sum = sum
    return max_sum
                
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largest_sum(arr))
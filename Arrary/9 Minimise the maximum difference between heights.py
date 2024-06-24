# Minimise the maximum difference between heights

def min_difference(arr,k):
    arr.sort()
    res = arr[len(arr)-1] - arr[0]
    
    tempMax =arr[len(arr)-1]
    tempMin =arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] < k:
            continue
        tempMin = min(arr[0]+k,arr[i]-k)
        tempMax = max(arr[i-1]+k,arr[len(arr)-1]-k)
        res = min(res,tempMax-tempMin)
        
    return res


k = 6
arr = [7, 4, 8, 8, 8, 9]
res = min_difference(arr, k)
print(res)
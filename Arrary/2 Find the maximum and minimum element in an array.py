#Find the maximum and minimum element in an array
def min_max(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            if arr[j] >= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
    print("Min :",arr[0])
    print("Max :",arr[len(arr)-1])

arr = [1, 8, 3, 7, 3, 5, 4]
min_max(arr)
    

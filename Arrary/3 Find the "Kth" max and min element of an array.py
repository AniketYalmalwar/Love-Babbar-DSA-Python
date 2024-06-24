#Find the "Kth" max and min element of an array
def kth_max(arr,k):
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            if arr[j] >= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
    return arr[len(arr)-k]

arr = [1, 8, 3, 7, 3, 5, 4]
k = int(input(f"Enter a number to finf kth max element between 0 to {len(arr)} : "))
print(kth_max(arr,k))
# find duplicate in an array of N+1 Integers 

def duplicate_elememnt(arr):
    for i in range(len(arr)-1):
        if arr[i] in arr[i+1:len(arr)]:
            return arr[i]
    
arr = [1,2,3,5,4,6,7,6]
print(duplicate_elememnt(arr))
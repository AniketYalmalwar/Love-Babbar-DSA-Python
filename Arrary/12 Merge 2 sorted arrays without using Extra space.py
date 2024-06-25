# Merge 2 sorted arrays without using Extra space 

def merge_arr(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]>arr2[j]:
                temp = arr1[i]
                arr1[i] = arr2[j]
                arr2[j] = temp
    print(arr1)
    print(arr2[::-1])

           
arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
merge_arr(arr1,arr2)

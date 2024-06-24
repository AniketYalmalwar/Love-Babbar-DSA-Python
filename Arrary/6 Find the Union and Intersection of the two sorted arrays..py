# Find the Union and Intersection of the two sorted arrays.

def union_intersection_array(arr1,arr2):
    arr=[]
    for i in arr2:
        if i in arr1:
            arr.append(i)
        if i not in arr1:
            arr1.append(i)
    return [arr1,arr]

arr1 = [1,2,3,6,4,5]
arr2 = [5,6,7,8,9,10]

result = union_intersection_array(arr1,arr2)
print("Union : ",result[0])
print("Intersection : ",result[1])
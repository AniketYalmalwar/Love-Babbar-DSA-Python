# find common elements In 3 sorted arrays 

def common_element(arr1,arr2,arr3):
    common_elements =[]
    for i in arr1:
        if i in arr2 and i in arr3:
            common_elements.append(i)
    return common_elements

arr1 = [1, 3, 4, 5, 7, 9, 10]
arr2 = [2, 3, 5, 7, 11, 12]
arr3= [3, 5, 7, 8, 9]
print(common_element(arr1,arr2,arr3))
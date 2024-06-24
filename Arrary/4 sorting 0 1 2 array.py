# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort_zero_one_two_array(arr):
    zero=one=two= 0
    for i in arr:
        if i==0:
            zero +=1
        elif i ==1:
            one +=1
        else:
            two +=1
        
    for i in range(len(arr)):
        if i<zero:
            arr[i]=0
        elif zero<=i <zero+one :
            arr[i] =1
        else:
            arr[i]=2
    
    return arr

arr = [2,0,1,0,1,2,1,1,0,2]
print(sort_zero_one_two_array(arr))
    

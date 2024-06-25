def merge_intervals(arr):
    arr.sort(key=lambda x: x[0])
    merged = []
    for i in arr:
        if not merged or merged[-1][1]<i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])
    return merged

arr = [[1,3],[2,4],[6,8],[9,10]]
print(merge_intervals(arr))

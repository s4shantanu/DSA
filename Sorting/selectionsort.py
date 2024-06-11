# selectoin sort

arr = [3,5,6,2,1,7]

def select(arr):
    n = len(arr)
    for i in range(n):
        start = i
        for j in range(i+1,n):
            if arr[j] < arr[start]:
                start = j
        arr[start], arr[i] = arr[i], arr[start]

select(arr)
print(arr)
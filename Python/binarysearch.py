#binary search 
arr = [1,3,4,9,13,20,21,25,30,31,35,40,45,50]
x = 21
n = len(arr)
s = 0
e = n-1 
while s<=e:
    mid = (s+e)//2
    if arr[mid] == x:
        print(mid)
        break
    elif arr[mid] < x:
        s = mid + 1
    else:
        e = mid - 1

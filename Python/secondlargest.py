arr = [2,4,5,7,89,55,3,1]

def print2largest(self, arr, n):
    largest = arr[0]
    seclargst = -1

    for i in arr:
        if i > largest:
            largest = i

    for j in arr:
        if j > seclargst and j < largest:
            seclargst = j

    return seclargst

print(print2largest(arr, len(arr)))
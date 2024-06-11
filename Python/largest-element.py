arr = [2,4,5,7,89,55,3,1]
def largest(arr):
    L=0;
    for i in arr:
        if i > L:
            L = i
    return L

largest(arr)
print(largest(arr))

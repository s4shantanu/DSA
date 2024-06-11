#Bubble sort
arr = [3,5,6,2,1,7]
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
        
bubblesort(arr)
print(arr)
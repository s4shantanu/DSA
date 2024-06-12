arr = [2,3,5,7,6,9,31,8]
i = 3
for j in range(len(arr)):
    if arr[j] == i:
        print("Element found at index", j)
        break
else:
    print("Element not found")

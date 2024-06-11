#insertion sort
def insert(arr):
    n = len(arr)  # Get the length of the array
    for i in range(1, n):  # Iterate over the array starting from the second element
        j = i  # Store the current index in a variable
        while j > 0 and arr[j] < arr[j-1]:  # Compare the current element with the previous element
            arr[j], arr[j-1] = arr[j-1], arr[j]  # Swap the elements if they are in the wrong order
            j -= 1  # Move to the previous index
            # The above two lines can also be written as:
            # temp = arr[j]
            # arr[j] = arr[j-1]
            # arr[j-1] = temp

insert(arr)  # Call the insert function to sort the array using insertion sort
print(arr)  # Print the sorted array
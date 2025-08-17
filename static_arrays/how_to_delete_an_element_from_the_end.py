def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = None
    else:
        print("The array is empty.")

my_array = [1,3,5]
length = len(my_array)

for _ in range(len(my_array) + 1):
    print(my_array)
    removeEnd(my_array, length)
    length -= 1
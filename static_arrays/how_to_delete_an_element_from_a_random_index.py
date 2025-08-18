def remove_element(arr, i):
    for index in range(i + 1, len(arr)):
        arr[index - 1] = arr[index]

def print_array(arr, length):
    for i in range(length):
        print(arr[i], end=" ")
    print()

arr = [1,3,5]
length = len(arr)

print_array(arr, length)

remove_element(arr, 0)
length -= 1

print_array(arr, length)
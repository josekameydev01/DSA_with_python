# Time complexity: O(N)
def insert(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index] = arr[index - 1]
    arr[i] = n


arr = [1,3,5]
length = len(arr)

print(arr)

insert(arr, 1, 8, length)

print(arr)

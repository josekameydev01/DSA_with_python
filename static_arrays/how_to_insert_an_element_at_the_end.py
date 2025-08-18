def insert(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

def print_array(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

arr = [0,0,0]

capacity = 3
length = 0

print_array(arr, length)

insert(arr, 1, length, capacity)
length += 1
print_array(arr, length)


insert(arr, 3, length, capacity)
length += 1
print_array(arr, length)

insert(arr, 5, length, capacity)
length += 1
print_array(arr, length)
#find the maximum and minimum elements in an array
def find_max_min(arr):
    max_value = max(arr)
    min_value = min(arr)
    return max_value, min_value

arr = [10, 20, 5, 40, 100, 1]
print("Array:", arr)

max_val, min_val = find_max_min(arr)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)
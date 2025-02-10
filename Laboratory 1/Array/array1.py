#reverse an array
def reverse_array(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)

reversed_arr = reverse_array(arr)
print("Reversed Array:", reversed_arr)

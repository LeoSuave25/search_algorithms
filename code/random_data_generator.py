import random

def generate_data(num):
    generated_set = [random.randint(1, 100) for _ in range(num)]
    return generated_set

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def write_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item},")

# Generate 10,000 random integers
sets = generate_data(10000)

# Sort the generated set
bubble_sort(sets)

# Write the sorted set to a text file
write_to_file(sets, 'sorted_random_integers.txt')

import random
import time
import sys
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) >= 3:
        pivot_candidates = random.sample(arr, 3)
        pivot = median_of_three(*pivot_candidates)
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr)
    return time.perf_counter() - start_time

sizes = [10_000, 50_000, 100_000, 500_000]
test_arrays = {size: [random.randint(-sys.maxsize - 1, sys.maxsize) for _ in range(size)] for size in sizes}

quick_sort_avg_times = []
randomized_quick_sort_avg_times = []

for size in sizes:
    print(f"Тестуємо розмір масиву: {size}")

    quick_sort_times = []
    randomized_quick_sort_times = []

    for _ in range(5):
        quick_sort_times.append(measure_time(quick_sort, test_arrays[size].copy()))
        randomized_quick_sort_times.append(measure_time(randomized_quick_sort, test_arrays[size].copy()))

    quick_sort_avg_times.append(sum(quick_sort_times) / len(quick_sort_times))
    randomized_quick_sort_avg_times.append(sum(randomized_quick_sort_times) / len(randomized_quick_sort_times))

    print(f"Quick Sort: {quick_sort_avg_times[-1]:.5f} секунд")
    print(f"Randomized Quick Sort: {randomized_quick_sort_avg_times[-1]:.5f} секунд\n")

plt.figure(figsize=(10, 6))
plt.plot(sizes, quick_sort_avg_times, label='Quick Sort', marker='o')
plt.plot(sizes, randomized_quick_sort_avg_times, label='Randomized Quick Sort', marker='o')

plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.title('Quick Sort vs Randomized Quick Sort Performance')
plt.legend()
plt.grid(True)
plt.yscale("log")
plt.show()

print("=== Аналіз результатів ===")
for i, size in enumerate(sizes):
    print(f"Розмір масиву: {size}")
    print(f"Середній час Quick Sort: {quick_sort_avg_times[i]:.5f} секунд")
    print(f"Середній час Randomized Quick Sort: {randomized_quick_sort_avg_times[i]:.5f} секунд\n")

print("=== Висновки ===")
print("1. Randomized Quick Sort, особливо з медіаною трьох, показує стабільніші результати.")
print("2. Відмінності у швидкості стають більш помітними на великих наборах даних.")
print("3. Використання `median_of_three` у Randomized Quick Sort зменшує ймовірність найгірших випадків.")

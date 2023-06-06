import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi ke-{i+1}: {arr}")

# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum pengurutan:", array)

start_time = time.time()
bubble_sort(array)
end_time = time.time()

print("Array setelah pengurutan:", array)
print("Waktu pengurutan:", end_time - start_time, "detik")

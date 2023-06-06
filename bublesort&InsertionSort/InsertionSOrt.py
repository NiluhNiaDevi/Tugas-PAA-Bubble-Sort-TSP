import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iterasi ke-{i}: {arr}")

# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum pengurutan:", array)

start_time = time.time()
insertion_sort(array)
end_time = time.time()

print("Array setelah pengurutan:", array)
print("Waktu pengurutan:", end_time - start_time, "detik")

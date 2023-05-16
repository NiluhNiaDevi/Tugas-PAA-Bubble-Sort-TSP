def bubble_sort(arr):
    n = len(arr)
    iter_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            iter_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            # Menampilkan proses iterasi
            print(f"Iterasi {iter_count}: {arr}")

        if not swapped:
            # Jika tidak ada pertukaran elemen pada iterasi ini,
            # array sudah terurut secara benar. Kita bisa keluar dari loop.
            break

    return iter_count


# Menguji fungsi bubble_sort
data = [64, 34, 25, 12, 22, 11, 90]
print("Data sebelum diurutkan:", data)

total_iter = bubble_sort(data)
print("Data setelah diurutkan:", data)
print("Total iterasi yang dibutuhkan:", total_iter)

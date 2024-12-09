def insertion_sort(data):
    for i in range(1, len(data)):
        elemen = data[i]
        j = i - 1
        while j >= 0 and data[j] > elemen:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = elemen
data = [99, 88, 77, 22, 33, 11, 55]
print("Data sebelum diurutkan:", data)
insertion_sort(data)
print("Data setelah diurutkan:", data)

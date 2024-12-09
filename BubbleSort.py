def bubble_sort(data):
    n = len(data)  
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
data = [80, 27, 25, 10, 29, 76, 50]
print("Data sebelum diurutkan:", data)
bubble_sort(data)
print("Data setelah diurutkan:", data)

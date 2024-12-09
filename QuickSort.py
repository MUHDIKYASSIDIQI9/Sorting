
def Quick_sort(data):
    if len(data) <= 1:
        return data  
    elemen_bagi= data[0]  
    data_kiri = [x for x in data[1:] if x <= elemen_bagi] 
    data_kanan = [x for x in data[1:] if x > elemen_bagi]  
    return Quick_sort(data_kiri) + [elemen_bagi] + Quick_sort(data_kanan)
data = [64, 39, 27, 19, 42, 11, 12]
print("Data sebelum diurutkan:", data)
data_terurut = Quick_sort(data)
print("Data setelah diurutkan:", data_terurut)

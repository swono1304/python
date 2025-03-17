# Import modul queue untuk menggunakan LifoQueue
from queue import LifoQueue

# Inisialisasi stack dengan kapasitas maksimum 3
stack = LifoQueue(maxsize=3)

# Menampilkan jumlah elemen dalam stack (sebelum ada elemen)
print(stack.qsize())  # Output: 0

# Menambahkan elemen ke stack menggunakan put()
stack.put('a')
stack.put('b')
stack.put('c')

# Menampilkan status penuh dan jumlah elemen
print("Full: ", stack.full())  # Output: True (karena stack sudah berisi 3 elemen)
print("Size: ", stack.qsize())  # Output: 3

# Menghapus elemen menggunakan get() (mengikuti prinsip LIFO)
print('\nElements yang dihapus dari stack:')
print(stack.get())  # Output: 'c'
print(stack.get())  # Output: 'b'
print(stack.get())  # Output: 'a'

# Menampilkan status kosong setelah semua elemen dihapus
print("\nEmpty: ", stack.empty())  # Output: True (karena stack sudah kosong)

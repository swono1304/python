# Import deque dari collections
from collections import deque

# Inisialisasi stack menggunakan deque
stack = deque()

# Menambahkan elemen ke stack (Push)
stack.append('a')
stack.append('b')
stack.append('c')

# Menampilkan stack sebelum elemen dihapus
print('stack:')
print(stack)  # Output: deque(['a', 'b', 'c'])

# Menghapus elemen dari stack (Pop)
print('\nElement dihapus dari stack:')
print(stack.pop())  # Menghapus 'c'

# Menampilkan stack setelah pop
print('\nStack setelah elements dihapus (pop):')
print(stack)  # Output: deque(['a', 'b'])

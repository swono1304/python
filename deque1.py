# Import deque dari collections
from collections import deque

# Inisialisasi stack menggunakan deque
stack = deque()

# Menambahkan elemen ke stack (Push)
stack.append('a')
stack.append('b')
stack.append('c')

# Menampilkan stack sebelum elemen dihapus
print('Stack awal:')
print(stack)  # Output: deque(['a', 'b', 'c'])

# Menggunakan appendleft() untuk menambah elemen di awal
stack.appendleft('x')
print('\nStack setelah appendleft(\'x\'):')
print(stack)  # Output: deque(['x', 'a', 'b', 'c'])

# Menggunakan pop() untuk menghapus elemen dari akhir (LIFO)
print('\nElement dihapus dari stack (pop):')
print(stack.pop())  # Menghapus 'c'

# Menampilkan stack setelah pop
print('\nStack setelah pop():')
print(stack)  # Output: deque(['x', 'a', 'b'])

# Menggunakan popleft() untuk menghapus elemen dari awal (FIFO)
print('\nElement dihapus dari awal (popleft):')
print(stack.popleft())  # Menghapus 'x'

# Menampilkan stack setelah popleft
print('\nStack setelah popleft():')
print(stack)  # Output: deque(['a', 'b'])

stack = []  # Membuat stack kosong

# append() untuk push elemen ke dalam stack
stack.append('a')
stack.append('b')
stack.append('c')

print('element stack')
print(stack)  # Output: ['a', 'b', 'c']

# pop() untuk menghapus elemen sesuai prinsip LIFO (Last In, First Out)
print('\nElement yang dihapus dari stack:')
print(stack.pop())  # Menghapus 'c'
print(stack.pop())  # Menghapus 'b'

print('\nStack setelah elements dihapus:')
print(stack)  # Output: ['a']

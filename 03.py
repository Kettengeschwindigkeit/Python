a = True
A = 3.14

print (a)                                             # -> True
print (A)                                             # -> 3.14
print (a, A)                                          # -> True 3.14
print ('\n')

a, b, c = 11, 22, 33

print (a, b, c)                                       # -> 11 22 33

a = 'Hello'
b = "Hello"

print (a, b)                                          # -> Hello Hello

print (len (a))                                       # -> 5 (длина строки)

# Конкатенация

print ('\n')

print (a + b)                                         # -> HelloHello

c = a + b

print (c)                                             # -> HelloHello

d = a + '=' + b

print (d)                                             # -> Hello=Hello

# Типы данных

g = 3
h = '3'
k = 'cpi0'

print (h + k)                                         # -> 3cpi0
# print (g + k)                                       TypeError: unsupported operand type(s) for +: 'int' and 'str'
print (str(g) + k)                                    # -> 3cpi0 (преобразование в строку)

print ('\n')

l = 8
m = '9'

# print (l + m)                                       # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print (str(l) + m)                                    # -> 89
print (l + int(m))                                    # -> 17

n = 9.1

print (l + n)                                         # -> 17.1

# Форматирование

n = 'Baby'
b = 'Nobody'

print ('Nobody puts ' + n + ' ' + 'in a corner')      # -> Nobody puts Baby in a corner
print ('Nobody puts {} in a corner'.format(n))        # -> Nobody puts Baby in a corner
print ('{} puts {} in a corner'.format(b, n))         # -> Nobody puts Baby in a corner

c = '{} puts {} in a corner'.format(b, n)

print (c)                                             # -> Nobody puts Baby in a corner

# Math

x = 11
y = 4
z = 12

print (x % y)                                         # -> 3 (остаток от деления)
print (z % y)                                         # -> 0

print (2 ** 4)                                        # -> 16 (возведение в степень)
print (9 ** 0.5)                                      # -> 3 (извлечение квадратного корня)

print (-5)                                            # -> -5
print (abs(-5))                                       # -> 5 (модуль числа)

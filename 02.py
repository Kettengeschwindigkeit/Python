# data output

print (444)                           # -> 444
print ('Hello')                       # -> Hello
print (44, 33, 'Hi')                  # -> 44 33 Hi
print (5, '6')                        # -> 5 6

# variables

foo = 6666
a = 5
helloPython = 9999
bar = 'Python'

print (foo, a)                        # -> 6666 5
print (a)                             # -> 5
print (foo + helloPython)             # -> 1665

a = 11
b = 12

print (a)                             # -> 11
print (a + b)                         # -> 23
print (a - b)                         # -> -1
print (a * b)                         # -> 132
print (a / b)                         # -> 0.9166666666666666

c = a + b
d = a - b

print (c)                             # -> 23
print (d)                             # -> -1

# float

f = 5.5
g = 0.5
h = .5

print (f, g, h)                       # -> 5.5 0.5 0.5

# data types

print (type (f))                      # -> <class 'float'>
print (type (b))                      # -> <class 'int'>
print (type (10 / 5))                 # -> <class 'float'>

k = True
K = False

print (k)                             # -> True
print (K)                             # -> False
print (type (k))                      # -> <class 'bool'>

a = 4
b = 6
c = (a + b) * 10

print (c)                             # -> 100

a = 5
b = 3
c = (a + b) * 10

print (c)                             # -> 80

def someFunction () :
  a = 1
  b = 3
  c = (a + b) * 10
  print (c)

someFunction()                        # -> 40
someFunction()                        # -> 40
someFunction()                        # -> 40

def anotherFuntcion () :
  c = (a + b) * 10
  print (c)

a = 1
b = 3
anotherFuntcion()                     # -> 40

a = 2
b = 4
anotherFuntcion()                     # -> 60

a = 3
b = 5
anotherFuntcion()                     # -> 80

# глобальные значения

f = 66

def ex1 () :
  f = 55
  f = f + 22
  print (f)

ex1()                                 # -> 77

def ex2 () :
  print (f)

ex2()                                 # -> 66

print (f)                             # -> 66

def ex3 () :
  global f
  f = 77
  print (f)

ex3()
print (f)

# аргументы

def ex4 (a, b) :
  c = (a + b) * 10
  print(c)
  return c

ex4(1, 2)
ex4(3, 4)
ex4(100, 50)

m = 100000 + ex4(3, 4)
print(m)

def ex5(s) :
  return ('Hello ' + s)

print(ex5('Lenin'))

def ex6 (n) :
  return n**2

result = ex6(5)
print (result)

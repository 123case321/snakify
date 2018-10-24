#Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Hi john
name = input()
print('Hi ' + name )

#Square
a = int(input())
print(a ** 2)

#Area of a right-angled triangle
a = int(input())
b = int(input())
print(a * b / 2)

#Hello Harry
name = input()
print('Hello, ' + name + '!')

#Apple Sharing
n = int(input())
k = int(input())
print (k // n)
print (k % n)

#Previous and next
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')

#Two timestamps
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

s1total = ((h1 * 60 * 60) + (m1 * 60) + s1)
s2total = ((h2 * 60 * 60) + (m2 * 60) + s2)

if s1total > s2total:
    sTotal = s1total - s2total
else:
    sTotal = s2total - s1total
    
print(sTotal)

#School Desks
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
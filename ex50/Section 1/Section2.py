#LastDigitOfInterger
a = int(input())
print(a % 10)

#TensDigit
n = int(input())
print(n // 10 % 10)

#SumOfDigits
n = int(input())
h = n // 100
t = n // 10 % 10
o = n % 10
print(h + t + o)

#FractionalPart
x = float(input())
print(x - int(x))

#FirstDigitAfterDecimalPoint
x = float(input())
print(int(x * 10) % 10)

#CarRoute
from math import ceil
n = int(input())
m = int(input())
print(ceil(m / n))

#DigitalClock
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)

#TotalCost
a = int(input())
b = int(input())
c = int(input())
cost = c * (100 * a + b)
print(cost // 100, cost % 100)

#ClockFace-1
h = int(input())
m = int(input())
s = int(input())
print(h * 30 + m * 30 / 60 + s * 30 / 3600)

#ClockFace-2
alpha = float(input())
print(alpha % 30 * 12)
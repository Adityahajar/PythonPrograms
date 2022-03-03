a = int(input("enter the 3 digit number:"))
b = a // 10   #
c = a % 100
d = c // 10
e = c % 10
f = d * 10 + e * 100 + b
print(f)
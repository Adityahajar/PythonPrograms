
n = int(input("enter a num"))
i = 1
a = 0

while i <= n:

    if n%i == 0:
        a = a+1
    i = i + 1
if a == 2:
        print("prime")
else:
        print("not prime")
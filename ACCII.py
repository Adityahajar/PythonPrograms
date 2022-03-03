a = ord(input("enter the char"))
#b = ord(a)
if a >= 65 and a <= 90:
    print("capital")
elif a >=97 and a <= 122:
    print("Small")
elif a >= 48 and a <= 57:
    print("Digit")
else:
    print("dont know")
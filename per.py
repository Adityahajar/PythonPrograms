M1 =  int(input("enter S1 mark"))
M2 =  int(input("enter S2 mark"))
M3 =  int(input("enter S3 mark"))
M4 =  int(input("enter S4 mark"))
M5 =  int(input("enter S5 mark"))

total = M1 + M2 + M3 + M4 + M5
per = total * 0.2

if per >= 90:
    print("grede A")
elif per >= 80:
    print("grede B")
elif per >= 70:
    print("grede C")
elif per >= 60 :
    print("grede D")
elif per >= 40:
    print("grede E")
else:
    print("Faile")



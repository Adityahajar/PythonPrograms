#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

num = []
for i in range(1500,2700):
    if (i % 7 == 0) and (i % 5 == 0):
        num.append (str(i))
print(",".join(num))



# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))

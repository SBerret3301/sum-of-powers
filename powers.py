import math 
x = int(input("enter a number : "))
a = 0
for i in range(0 , x+1) :
    a = a + pow(10 , i)
print(a)
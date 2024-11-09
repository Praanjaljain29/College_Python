#question 1
print("factorial of a give number")
num=int(input("Enter a number: "))
f=1
if num<0:
    print("factorial number is not defined")
elif num==0:
    print("factorial of = 1")
elif num==1:
    print("Factorial = 1")
else:
    for i in range(1,num+1):
        f=i*f
        i+=1
    print("factorial of ", num," is ", f)
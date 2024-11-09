#question4
print("Fibonacci series")
num=int(input("Enter till wher you want the fibbonacci series to be printed: "))
a=0
b=1
if num==1:
    print(0)
elif num<0:
    print("Wrong input")
elif num==0:
    print("Wrong input")
elif num==2:
    print("0 1")
elif num>2:
    print(a,end=" ")
    print(b,end=" ")
    while num!=0:
        s=a+b
        print(s,end=" ")
        a=b
        b=s
        num=num-1

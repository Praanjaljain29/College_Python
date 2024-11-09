#question 2
print("armstrong number")
num=int(input("Enter a number to check whether the nummber is armstrong number: "))
c=len(str(num))
copy=num
arm=0
while num!=0:
    p=(num%10)**c
    arm=arm+p
    num=num//10
if arm==copy:
    print(copy," is a armstrong number")
else:
    print(copy," is not a armstrong number")
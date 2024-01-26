#question 6 
print("sum of digits")
num=int (input("Enter a number to find the sum of digits: "))
t=0
while num!=0:
    t=t+num%10
    num=num//10
print("The sum of digits is ",t)
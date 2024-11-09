#question 5
print("Palindrome number")
num=int(input("Enter a number: "))
rev=0
copy=num
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if copy==rev:
    print(copy," is palindrome number")
else:
    print(copy," is not palindrome number")
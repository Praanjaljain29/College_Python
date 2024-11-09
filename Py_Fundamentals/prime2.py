#question 9
for n in range(1,101):
   a=0
   for i in range (1,n+1):
       if n%i==0:
        a=a+1
   if a==2:
    print(n)
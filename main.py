def fact1(n):
 if n==0 or n==1:
   return 1
 else:
   return n*fact1(n-1)
number=int(input("Enter value:"))
res=fact1(number)
print("The factorial of {} is {}.". format(number,res))
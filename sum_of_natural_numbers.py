num = int(input("Enter a number : "))
a = num
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
num = a
print("The sum of natural numbers upto",num,"is",sum)

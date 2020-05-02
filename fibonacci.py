f1, f2 = 0, 1
cnt = 0
num = int(input("Enter the number of terms:"))
# check if the number of terms is valid
if num <= 0:
   print("Enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(f1)
else:
   print("Fibonacci sequence upto",num,":")
   while cnt < num:
       print(f1)
       temp = f1 + f2
       f1 = f2
       f2 = temp
       cnt = cnt + 1

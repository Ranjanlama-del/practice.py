#a = int(input("Enter the number: "))
#if a >= 18:
#    print("You are eligible to vote.")
#elif a < 18:
 #   print("You are not eligible to vote.")
#else:
#    print("Invalid input.")
money = 0
a = (input("do you want to check your balance: "))
if a.upper() == "Y":
    print("Your balance is: ", money)
else:
     exit()  
b = (input("would you like to deposit an amount: "))
if b.upper() == "Y":
   print("Enter the amount you want to deposit:")
b = int(input())
money += b
print("Your added balance is: ", money)
c = (input("would you like to withdraw an amount: "))
if c.upper() == "Y":
    print("Enter the amount you want to withdraw:")
    c = int(input())
    money -= c
    print("your remaning balance is : ", money)

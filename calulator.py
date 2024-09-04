print("   --Simple calculator--     ")

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the second number here: "))
print("press 1 for Additon \npress 2 for Substraction \npress 3 for Multiplication \npress 4 for Division")

choice = int(input("enter your choice 1-4: "))
if choice == 1:
    print("The Additon of given two number is",num1 + num2)
elif choice == 2:
    print("The Substraction of given two number is",num1 - num2)
elif choice == 3:
    print("The Multiplication of given two number is",num1 * num2)
elif choice == 4:
    print("The Divison of given two number is",num1 / num2)
else:
    print("Invalid input")
    
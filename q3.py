# User will input (2numbers).Write a program to swap the numbers
Num1 = input("Enter Number 1 of your choice:") 
Num2 = input("Enter Number 2 of you choice:")
print("Before Swaping the Numbers:", Num1, ',' ,Num2)
Num1, Num2 = Num2, Num1
print("After Swaping the Numbers:", Num1, ',' ,Num2)
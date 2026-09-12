# User will input (3ages).Find the oldest one
age1 = input("Enter age1:")
age2 = input("Enter age2:")
age3 = input("Enter age3:")
if age1 > age2 and age1 > age3:
    print("Oldest is:", age1)
elif age2 > age1 and age2 > age3:
    print("Oldest is:", age2)
else:
    print("Oldest is:", age3)
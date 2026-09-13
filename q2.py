# Write a program that will convert celsius value to fahrenheit
try:
    C = (input("Enter temprature (in celcuis) value:"))
    F = (float (C)  * 9/5) + 32
    print("The value in F is:", F)   
except ValueError:
    print("Please enter a number.") # if someone tries  to enter string
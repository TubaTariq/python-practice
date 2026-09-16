# Write a program that will give you the sum of 3 digits
try:
  numbers = input("Enter numbers separated by spaces: ")
  my_list = [float(num) for num in numbers.split()]
  print("the sum of numbers is:")
  print(sum(my_list))
except ValueError:
  print("Invalid Entry")
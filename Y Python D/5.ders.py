# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))
# current_year = int(input("Enter current year: "))
# year = 2023 / 10

# age = current_year - birth_year
# is_adult = age >= 18

# if is_adult:
#     print("you can vote")
#     print(1)
#     if True:
#         print(5)

# if age >= 18:
#     print("You can vote!")
#     print("if e ait")

# print("selam")
# if age <= 18:
#     print("Sorry You cant vote :-(")

#1- Syntax error
#2 - Runtime error
# x = 10
# y = 0
# result = x / y

# print(f"{x} divided by {y} is {result}")
# 3- logical error
hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages *= 2

print(f"Daily wages: {daily_wages} euros")
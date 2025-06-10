#1. Take user's name and age as input and print:
# name = input('what is your name')
# print('welcome, ', name)

# name = input('What is your name? Ans: ')
# age = input('what is your age? Ans: ')
# print('Your name is: ', name, 'and Your age is: ', age)

#2. Take two numbers as input and perform:
# num1 = float(input('Enter your 1st Num: '))
# num2 = float(input('Enter your 2nd Num: '))
# average = (num1 + num2) / 2
# print('Sum of those number is: ', num1+num2)
# print('Average of those number is: ', average)

# age = float(input('Enter your age: '))
# if age >= 18:
#     print('You are adult.')
# else:
#     print('You are not adult.')



############ 100 days python course ############
###########
# Write your code below this line 👇
# print('Hello' + input('what is your name?') + '?')


###########
# name = input('What is your name?\n')
# length = len(name)
# print("Your name length is: " + str(length))

###########
# a = 29
# b = 41

# print('a: ' + str(a))
# print('b: ' + str(b))


########### Band Name Generator
# print('Welcome to the Band Name Generator.')
# city = input('What city did you grow up in?\n')
# pet = input('What is the name of your pet?\n')
# print('Your band name could be ' + city + ' ' + pet)


###########
# two_digit_number = input('Enter two digit number: ')
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print("Your number is: ", + first_digit+second_digit)


########### BMI Calculator
# height = float(input('Enter your height in meters: '))
# weight = float(input('Enter your weight in Kilograms: '))
# bmi = round(weight / height ** 2 , 1)

# if bmi <= 18.5:
#     print(f'Your BMI is: {bmi} | You are underweight.')
# elif 18.5 < bmi <=24.9:
#     print(f'Your BMI is: {bmi} | You are normal weight.')
# elif 24.9 < bmi <= 29.9:
#     print(f'Your BMI is: {bmi} | You are overweight.')
# else:
#     print(f'Your BMI is: {bmi} | You are obese.')


########### your life in weeks
# age = int(input('Enter your age in years: '))

# life_in_days = age * 365.25
# your_life_in_weeks = life_in_days / 7


# total_life_in_weeks = int(90*52)
# weeks_remaining = total_life_in_weeks - your_life_in_weeks

# print(f'Your total life sepnd in weeks: {round(your_life_in_weeks,1)}')
# print(f'Your total remaining life in weeks: {round(weeks_remaining,1)}')


########### Tip Calculator
# bill = float(input('What was the total bill?\n'))
# tips = float(input('How much tip would you like to give? 10, 12, or 15?\n'))
# total_people = int(input('How many people to split the bill?\n'))

# total_tips = round((bill / 100) * tips, 2)
# total_bill = round(bill+total_tips, 2)
# each_person_bill = round(total_bill / total_people, 2)

# print('Each person should pay: ', each_person_bill)


########### Rollercoaster
# print('Welcome to the Rollercoaster')
# height = int(input('What is your height in cm? '))

# if height > 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('You can not ride the rollercoaster')


########### Even or odd number check
# number = int(input('Which number do you want ot check? '))
# if number % 2 == 0:
#     print('This number is Even Number.')
# else:
#     print('This number is Odd Number.')


########### rollercoaster ticket - if nested elif else statement
# print('Welcome to the rollercoaster!')
# height = int(input('Enter your height in cm: '))

# if height >= 120:
#     print('You can ride the rollercoaster.')
#     age = int(input("Enter your age: "))
#     if age < 12:
#         print('Please pay $5')
#     elif age <= 18:
#         print('Please pay $7')
#     else:
#         print('Please pay $12')
# else:
#     print('You are not allow to ride.')



########### BMI Calculator 2.0
# height = float(input('Enter your height in Meeter: '))
# weight = int(input('Enter your weight in kg: '))

# bmi = weight / (height * height)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")



########### Leap Year
# year = int(input('Write your carent year: '))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print('Leap Year')
#     else:
#       print('Not Leap Year')
#   else:
#     print('Leap Year')
# else:
#   print('Not Leap Year')


########### rollercoaster ticket 2.0
# print('Welcome to the Rollercoaster!')
# height = int(input('Enter your height in cm: '))
# bill = 0

# if height >= 120:
#   print('You can ride the rollercoaster.')
#   age = int(input('What is your age? '))
#   if age < 12:
#     bill = 5
#     print('Child tickets are $5')
#   elif age <=18:
#     bill = 7
#     print('Youth tickets are $7')
#   else:
#     bill = 12
#     print('Adult tickets are $12')
    
#   wants_photo = input('Do you want a photo taken? Y or N. ')
#   if wants_photo == 'Y' or wants_photo == 'y':
#     bill += 3
#     print(f'\n\nYour final bill is:\n--------------------\nTickets price + Photo price($3) = ${bill}\n\n')
#   else:
#     print(f'Your final bill is: {bill}')
# else:
#   print('You are not allow to ride')


########### Pizza Order
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input('Small pizza (S): $15\nMedium pizza (M): $20\nLarge pizza (L): $25\nWhat size pizza do you want? S, M, or L: ')
# add_pepperoni = input('\npepperoni for small pizza  = $2\npepperoni for medium or large pizza = $3\nAdd pepperoni for small pizza (Y or N): ')
# extra_cheese = input('\nExtra cheese = $1\nDo you want extra cheese? Y or N: ') 

# bill = 0

# if size == 'S':
#   bill = 15
#   if add_pepperoni == 'Y':
#     bill += 2
# elif size == 'M':
#   bill = 20
#   if add_pepperoni == "Y":
#     bill += 3
# elif size == 'L':
#   bill = 25
#   if add_pepperoni == "Y":
#     bill += 3
# else:
#   print('Please enter valid input and try again. Thank you.')

# if extra_cheese == 'Y':
#   bill += 1
#   print(f'Your final bill is: {bill}')
# else:
#     print(f'Your final bill is: {bill}')
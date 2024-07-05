#Instrukcje warunkowe

# JAK CHCESZ KOMENTOWAĆ TO ZAZNACZASZ KOD MYSZKA I CTR+/

#1 The program checks your height and age, becasue we have to know, that you can ride a rollercoaster
#mamy warunek na wzrost potem nilety w zaleznosci do wieku i czy chce zdjecie dodatkowe i na koniec dodane, ze jak masz wiek sredni 45-55 lat to za darmo
# print(" Welcome to the rollercoaster! ")
# height = round(float(input(" What is your height in cm? ")),3) #od razu nam zaokrągla wartośc do 3 miejsc po przeicnku, daliśmy float, bo ktos może znać dokładnie 
# age = int(input(" What is your age? "))
# print(height, age)
# bill = 0
# if height >= 120 and age > 12:
#     print( f" You can ride on rollercoaster, because you have {height} cm ")
#     if age <= 12:
#         bill = 5
#         print("Child tickets are 5$")
#     elif age > 12 and age <= 18:
#         bill = 7
#         print("Youth tickets are 7$")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us")
#     else:
#         print("Adult tickets 12$")
#         bill = 12
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your total bill = {bill}")

# else:
#     print(f" You can't ride on rollercoaster. You must be 120cm, but you have only {height} ") 

# #2 The program checks whether th enumner is even or odd (parzysta - even, odd - nieparzysta)

# print(" What number do you choose? Please write it, otherwise the program will not work ")
# number = int(input(" I choose the number: "))

# if number % 2 == 0: #modulo, daje nam reszte z dzielenia 
#     print(" The number is oven - parzysta")
# else:
#     print(" The number is odd -nieparzysta")

# #3 BMI - upgrade

# print(" What is your BMI? ")
# height = float(input("Could you provide your height in meters? "))
# weight = float(input(" Could your provide your weight? "))
# BMI = round(float(weight / (height ** 2)),3)

# if BMI < 18.5:
#     print(f" Your BMI is {BMI} and you are underweight")
# elif BMI >= 18.5 and  BMI < 25:
#     print(f" Your BMI is {BMI} and you are normal weight")
# elif BMI >= 25.0 and BMI < 30:
#     print (f" Your BMI is {BMI} and you are slightly overweight")
# elif BMI >= 30.0 and BMI < 35:
#     print (f" Your BMI is {BMI} and you are obese")
# else:
#     print (f" Your BMI is {BMI} and you are clinically obese")

# #4 Leap year, jest na to algorytm, jezeli jest podzielne przez 4 bez reszty, z wyjatkiem podzielnego przez 100, chyba ze jest tez podzielny przez 400 v 
# print ("Is it Leap or normal year ")
# number = int(input(" Please provide your year: "))

# if number % 4 == 0 and number % 100 == 0 and number % 400 == 0:
#     print("Year is Leap")
# elif number % 4 == 0 and number % 100 == 0 and number % 400 != 0:
#     print("Year is normal")
# elif number % 4 == 0 and number % 100 !=0:
#     print("Year is Leap")
# else:
#     print("Year is normal")

# #5 Leap year v2  #łatwiejsze bo sprawdza nam po kolei jakby jak jest w if kolejny if to sprawdza kolejny warunek po spelnieniu poprzedniego
# print ("Is it Leap or normal year ")
# number = int(input(" Please provide your year: "))

# if number % 4 == 0:
#     if number % 100 == 0:
#         if number % 400 == 0:
#             print("The year is Leap")
#         else:
#             print("The year is normal")
#     else:
#         print("The year is Leap")    
# else: 
#     print("The year is normal")

#6 - Automatic pizza order

# print("Than you for choosing Python Pizza Delivers")
# size = input("Could you provide what size do you want? S, M, L  ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1   

# print(f"Your final bill is: {bill}")


#7 The love calculator, czyli 2 imiona i nazwiska i ile w nich wystepuje liter ze slow LOVE i TRUE, sprawdzamy dla Brad Pitt i Jennifer Aniston

# print(" The love calculator is calculating your score..")
# name1 = input("What is your name? ")
# name2 = input("What is their name? ")
# combined_names = name1 + name2
# lower_names = combined_names.lower() #daje nam te litery na małe, żeby wszystkie sie zliczaly

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")

# first_digit = t+r+u+e  #pierwsza cyfra

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")

# second_digit = l+o+v+e #druga cyfra

# score = int(str(first_digit) + str(second_digit)) #mamy wynik zalozmy 7 i 6, czyli dostaje 76 w str, ale zamieniam na int zeby porownac z liczbami

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together")
# else:
#     print(f"your score is {score}.")

#8 Treasure island - wyspa skarbów, gra

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 

direction = input("Where will you go? Right or Left? ")
direction_lower = direction.lower()

if direction_lower == "left":
    conveyance = input(" What mode of transportation will you choose? Swim or Boat ")
    conveyance_lower = conveyance.lower()
    if conveyance_lower == "boat":
        door = input(" Which door will you choose? Red, Blue or Yellow ") 
        door_lower = door.lower()
        if door_lower == "yellow":
            print(" You win! :) ")
        elif door_lower == "red":
            print(" You loose! ")
        else:
            print(" You were eaten by beasts - so you game over")
    else:
        print(" You were attacked by a trout - so you game over ")    
else:
    print(" You fell into a hall, so you game over :( ")


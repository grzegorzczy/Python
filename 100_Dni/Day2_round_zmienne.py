#Data Types

#String

print("Hello"[0])

print(123 + 123)

#Float - zmiennoprzecinkowe

3.14169

#Boolean 
True 
False

a=float(123)
print(type(a)) #mowi nam jaki to typ

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#count
3+4
7-4
3*2
6/3
2**3

#BMI = weight/heigt^2
print("Kalkulator BMI: ")
weight = float(input("Podaj swoją wagę: "))
height = float(input("Podaj swój wzrost: "))

# weight_as_float = float(weight)
# height_as_float = float(height)

BMI = round( weight/(height**2), 2) #round daje nam zaokrąglenie liczby. 2- ilosc mejsc po przeicnku
print(BMI)

#skrócony zapis

score = 0
score =+ 1 #można użyc tez -, *, /
print(score)

#f-String
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

#counting of weeks to finish your life
print("Your life in weeks")
normal_age = int(input("How old is it "))
die_age = int(input("When will it die? "))
year = 52
substraction = (die_age - normal_age) * year 

print(f"You have {substraction} weeks left.")


#Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input('How much tip would you like to give? 10%, 12% or 15%'))
people = int (input("How many people to split the bill?" ))
price = (bill + (tip/100 * bill))/people
end_price = round(price ,2) #zaokraglenie do 2 miejsc
end_price2 = "{:.2f}".format(price) #drugi sposób zaokrąglenia
print(f"Each person should pay: {end_price2}") #wypisanie calkowitej ceny
# #Loop pętla for, przechodzi po kolei przez liste, 

# fruits = ["Apples", "Peach", "Pear"]

# for fruit in fruits: #fruit to nasza zmienna, która sobie przyporządkowuje po kolei z listy
#     print(fruit)
#     print(fruit + " Pie ")

#1 average student heiht

# height_student = [156, 178, 165, 171, 187]

# total_height = 0

# for x in height_student: #czyli najpierw total mamy zero potem nasz x przechodzi przez liste i przypisuje co pietle do taj wartosc i na koncu ja wypisuje
#     total_height += x
# print(f"total height = {total_height}")

# number_of_studnets = 0

# for y in height_student:
#    number_of_studnets += 1
# print(f"number of students = {number_of_studnets}")

# average_height = round(total_height/number_of_studnets)
# print(f"average height = {average_height}")

# #2 High score from a list score

# high_score = 0
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# for z in student_scores: #przeszukuje w liście i przypisuje do z, jezeli jakis z jesy wiekszy od hihh_score(startuje od 0), to przypisuje do z i sprawdzam dalej 
#     if z > high_score:
#         high_score = z

# print(f"The highest socre is: {high_score}")


#hight score v2

# score = [10, 20, 30, 40, 50, 60]

# sum_score = 0

# for x in score:
#     sum_score += x
# print(f"Your sum score is {sum_score}")

# number_of_score = 0
# for x in score:
#     number_of_score += 1
# print(f"Your number of score are: {number_of_score}")

# average_score = print(f" Your average score is {round(sum_score/number_of_score)}")

# high_score = 0

# for x in score:
#     if x > high_score:
#         high_score = x
# print(f"Your high score is : {high_score}")

# #3Pętla liczby, with range

# for number in range(1,11):
#     print(number)

# total_sum = 0
# for number in range(1,101):
#     total_sum += number
# print(total_sum)

#4 Calculator
# print("Calculator")  #liczy nam sume od 2 do liczby X+1 i to dla liczb  parzystych, bo zaczynamy od 2

# X = int(input(" write a number from which we would sum. Number X= "))
# sum = 0
# for x in range(2 ,X+1, 2):
#     sum += x
# print(sum)

# Calculator v2 - wykorzystanie modulo
# print("Calculator")  #liczy nam sume od 2 do liczby X+1 i to dla liczb  parzystych, bo zaczynamy od 2

# X = int(input(" write a number from which we would sum. Number X= "))
# sum2 = 0
# for x in range(1 ,X+1):
#     if x % 2 == 0:
#         sum2+=x
# print(sum2)

#5 Fizz Buzz
# x=100
# for x in range(1,x+1):
#     if x % 3 ==0 and x % 5 ==0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print(" Fizz ")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x) 


# 6 Password generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# password =" "

# for letter in range(1, nr_letters + 1): #przechodzi nam załózmy 4 razy
#     password += random.choice(letters) #dodaje do zmiennej passowrd randomowo w kazdym obiegu petli litera

# for number in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# for symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list =[]

for letter in range(1, nr_letters + 1): #przechodzi nam załózmy 4 razy
    password_list += random.choice(letters) #dodaje do zmiennej passowrd randomowo w kazdym obiegu petli litera

for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = " "
for char in password_list:
    password += char
print(f"You password is: {password}")

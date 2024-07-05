#Random module

import random
# import Dayz4_1

# print(Dayz4_1.pi) #tak sie importuje z innego pliku

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random() #zmiennoprzecinkowa [0,1)
# print(random_float)

# #1 Heads or Tails - orzeł (1) czy reszka (0)

# random_side = random.randint(0,1)

# if random_side == 0:
#     print( "It's Tails")
# else:
#     print("It's Heads")

#2 List - maja ustaloną kolejność, można odwoływac sie do -1, to ostatnia rzeecz z listy itd

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
# print(states_of_america[0])

# states_of_america[1] = "Pennsylwania" #zmienia się
# print(states_of_america)

# states_of_america.append("Georgia") #dodawanie na końcu
# print(states_of_america)

# states_of_america.extend(["Nep Hampshire", "Virginia"]) #można dodać listę do listy, czyli wiele elementów
# print(states_of_america)

#3 Who pay for dinner?

# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"] #tworze liste

# num_items = len(names) #ilość elemntow w liscie

# random_name = random.randint(0, num_items - 1) # random liczba z listy
# who_is_paying = names[random_name] #przypisanie wylosowanej liczby do osoby z listy, tak jakby zrobis names[1]
# print(f"Today people who is paying is {who_is_paying}")

#4Zagnieżdzona lista 

# fruits = ["Strawberies", "Apples", "Grapes"]
# vegetables = ["Spinach", "Tomatoes", "Potatoes"]
# dirty_dozen = [fruits, vegetables] #brudna lista, pestycydy

# print(dirty_dozen)

#5 Umieszczenie x na planszy

#          #a    #b   #c
# line1 = [" ", " ", " "] #1 
# line2 = [" ", " ", " "] #2
# line3 = [" ", " ", " "] #3 

# map = [line1, line2, line3]
# print("Hiding your treasure! x marks the spot")

# position = input("Write position letter and number") #podaje pozycje np. B1

# letter = position[0].lower() #pobiera mi litere B, chodzi ogolnie o litere
# abc = ["a", "b", "c"] 
# letter_index = abc.index(letter) # abc - zbior mozliwosci i przyporzadkwuje index z litery, Zwraca indeks (pozycję) pierwszego wystąpienia podanego znaku (w tym przypadku letter) w łańcuchu abc.
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "x"

# print(f"{line1}\n{line2}\n{line3}\n")



# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]

# map = [line1, line2, line3]
# print("Hiding your treasure! x marks the spot")
# position = input("Provide your position" )

# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) -1

# map[number_index][letter_index] = "x"


# print(f"{line1}\n{line2}\n{line3}")


#5 Rock paper scisors 

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(" Hello it's rock paper scisors game! :) ")

list_images = [rock, paper, scissors]

user_choice = int(input(" What do you choose? Type 0 for Rock, type 1 for Paper and type 2 for Scissors \n"))

if user_choice >= 3 or user_choice < 0:
    print(" You typed an invalid number, you lose! ")
else:
    print(f" You chose {user_choice}")
    print(list_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f" Computer chose {computer_choice}")
    print(list_images[computer_choice])

    if user_choice == computer_choice:
        print(" It' draw ")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! ") 
    elif user_choice == 1 and computer_choice == 0:
        print("You lose! ")
    elif user_choice > computer_choice:
        print(" You win! ")     
    elif user_choice < computer_choice:
        print(" You lose! ")











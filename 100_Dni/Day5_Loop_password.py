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

score = [10, 20, 30, 40, 50, 60]

sum_score = 0

for x in score:
    sum_score += x
print(f"Your sum score is {sum_score}")

number_of_score = 0
for x in score:
    number_of_score += 1
print(f"Your number of score are: {number_of_score}")

average_score = print(f" Your average score is {round(sum_score/number_of_score)}")

high_score = 0

for x in score:
    if x > high_score:
        high_score = x
print(f"Your high score is : {high_score}")
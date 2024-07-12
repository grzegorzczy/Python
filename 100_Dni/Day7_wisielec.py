#hangman
import random
from Day7z1 import word_list
from Day7z2art import stages, logo
random_word = random.choice(word_list)
word_length = len(random_word)
print(f"Word which you have to guess: {random_word}")

end_of_game = False
lives = 6 #ta zmienna jest odpowiedzialna za zliczanie życ
print(logo)

display = []
for _ in range(word_length): # _ - bp raz sie tylko odwołuje
    display += "_"
#print(display)



while not end_of_game: #petla nieskonczona jak jest true, czyli tera, jak wartosc end of game bedzie miec true t bedzie false i sie zatrzyma (EZ)
    guess_letter = input(str("Guess a letter: ")).lower()

   
    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length): # zasieg range od 0 do 1 - gdzie 1 to długośc całego słowa
        letter = random_word[position]
        #print(f"Current postion: {position}\n")
        # f"Current letter: {letter}\n" 
        # f"Guessed letter: {guess_letter}")

        if letter == guess_letter:
            display[position] = letter
        #print(display)

    if guess_letter not in random_word: #odpowiada za odejmowanie żyć
        print(f"You guessed {guess_letter} that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")
    
    if "_" not in display: #odpowiada za to, ze jak w liscie zabraknie "_" to wygralismy
        end_of_game = True
        print("You win")

    print(stages[lives])
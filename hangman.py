
import random
import hangman_words
from hangman_art import logo,stages
print(logo)
#Task1- import a random word from the hangman words and make it the chosen word
chosen_word=hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)]
#print(chosen_word)
#Task2- Create blanks for the word
display=[]
for i in range(0,len(chosen_word)):
    display.append('_')
print(display)
#Task3- Ask the user to guess the word
#Task6- Counting the lives according to the stages
lives=len(stages)
#print(lives)

#Task5- Perform Task3 and Task4 continously till there are no blank spaces left in the display
end_of_game=False #This marks that the game has not ended yet
while(end_of_game==False):
    guess=input("Guess a letter: ").lower() #Task3
    #Task8 - If the guess letter has already been guessed
    if guess in display:
        print(f"The letter {guess} has already been guessed.")
    #Task4 - Check if the letter is present in the chosen word or not.If yes,replace that _ with the letter
    for position in range(0,len(chosen_word)):
        letter=chosen_word[position]
        if(letter==guess):
            display[position]=guess
    
    print(display)
    #Task7 - Reducing the number of lives when wrong letter is guessed
    if guess not in chosen_word:
        lives-=1
        print(f"The letter {guess} is not present in the word.")
        print(stages[lives])
        if lives==0:
            end_of_game=True
            print(f"The word is {chosen_word} ,you lost!")
    if '_' not in display:
        end_of_game=True
        print(f"The word is {chosen_word} ,you won!")

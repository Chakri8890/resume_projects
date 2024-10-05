import random
import hangman_fugure
word_list=["apple","pineapple","mango"]

lives = 6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+= '_'
print(display)
game_over=False
while not game_over:
    guess_any_letter=input("enter a letter to guess:")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess_any_letter:

         display[position]=guess_any_letter
    print(display)
    if guess_any_letter not in chosen_word:
        lives=lives-1
        if lives == 0:
            game_over=True
            print("you lose the game")
            if '_' not in display:
                if game_over==True:
                    print("you win")
    print(hangman_fugure.diagram[lives])




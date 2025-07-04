import random

word_list = ["aardvark"," buffalo", "cat", "dog"]
chosenWord = random.choice(word_list)
print(chosenWord)

placeHolder = ""
wordLen = len(chosenWord)
for position in range(wordLen):
    placeHolder += "_"
print(placeHolder)



game_over = False
correct_letters=[]


while not game_over:
    guess = input("Guess a letter ").lower()
    display = ""

    for letter in chosenWord:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("You win")





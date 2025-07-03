import random

word_list = ["aardvark"," buffalo", "cat", "dog"]
chosenWord = random.choice(word_list)
print(chosenWord)
guess = input("Guess a letter ").lower()

placeHolder = ""
wordLen = len(chosenWord)
for position in range(wordLen):
    placeHolder += "_"

display = ""
for letter in chosenWord:
    if(letter == guess):
        display += letter
    else:
        display += "_"



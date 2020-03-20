from random_word import RandomWords
r = RandomWords()
print("Starting a game of Hangman")
x = True
while x:
    try:
        a = input("\nHow many incorrect guesses do you want? [1~25] : ")
        guess = int(a)
        if guess < 1 or guess > 25:
            x = True
            print("Please enter an integer between 1 and 25 (both inclusive)")
        else:
            x = False
    except:
        print("Please enter a valid integer for the number of guesses")

x = True
while x:
    try:
        b = int(input(("What maximum word length do you want? [2~15] : ")))
        length = int(a)
        if length < 2 or length > 15:
            x = True
            print("Please enter an integer between 2 and 15 (both inclusive)")
        else:
            x = False
    except:
        print("Please enter a valid integer for the length of the word")

list = []
print("\nSelecting a word")
print("Please wait...")
word = r.get_random_word(hasDictionaryDef="true",maxLength=b)
count=0
print("\nPlease enter all letters in lower case")
print("Do not enter the same letters repeatedly...")
word.lower()
while guess >= 0 and count <= b :
    letter = input("\nEnter a letter : ")
    while letter in list:
        print("You have already entered this letter before")
        print("Please enter a different one")
        letter = input("\nEnter a letter : ")
    list.extend(letter)
    occ = word.count(letter)
    if occ == 0:
        print(letter,"is NOT IN the word!")
        guess -=1
    elif occ==1:
        print(letter,"is IN the word!")
    else:
        print(letter,"is IN the word and it occurs",occ,"TIMES IN the word!")
    count += occ
    print("Attempts remaining : ",guess)
if count == b:
    print("\nCongratulations! You have guessed the word correctly!")
    print("\nThe word is",word)
else:
    print("\nSorry! You have run out of attempts :( ")
    print("Better luck next time")
    print("\nThe secret word was",word)

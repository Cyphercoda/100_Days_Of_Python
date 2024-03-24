import random

# create a Greeting

print("Welcome to the HangMan!")
# create your wordlist
word = ["hackerrank", "hackerrank.com", "Bounty", "hacker", "hackerspot"]
# random choose a word from your wordlist you have created
secret_word = random.choice(word)
# ask the user to guess a letter
user_input = input("Please guess a letter").lower()
print(user_input)
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word.
for letter in secret_word:
    if letter == user_input:
        print("RightH")
    else:
        print("Sorry")
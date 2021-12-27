import random
import string
print("Welcome to Password Picker")

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(10, 1000)
    # special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number)
    print("You Password is : %s" % password)

    response = input("Would you like another password? Type Y or N: ")
    if response.upper() == 'N':
        break

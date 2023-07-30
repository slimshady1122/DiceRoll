import random
word = random.choice(["RECURSION", "ITERATION", 'CONDITIONS', 'PROGRAMMING', 'VARIABLES'])
unknown = len(word) * '_'  #TO PRINT THE  WORD TO BE GUESSES IN THIS FORMAT ________
print(unknown)

while True:
    enterToPlay = input(str("press Enter to reveal a letter [q to quit]"))
    if enterToPlay == "q":
        break

    else:
        ind = random.randint(0, len(word) - 1)

        print("The Letter revealed is", word[ind])

        unknown = unknown[0:ind] + word[ind] + unknown[ind + 1:]
        print(unknown)
        if unknown == word:
            break




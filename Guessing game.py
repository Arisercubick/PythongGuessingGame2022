import sys

wrongdiff = 0
user_score = 0
admin_control = 0
username = input("Insert Username: ")
guess_limit = 0
difficulty = input("Please select difficulty.\n e for easy, a for average, h for hard, and d for death: ")
while difficulty != "e" and difficulty != "a" and difficulty != "h" and difficulty != "d" and difficulty != "admin":
    difficulty = input("Please write it correctly(Do not capitalize).\ne for easy, a for average, h for hard, and d for death: ")
else:
    if difficulty == "e":
        guess_limit = 5
    elif difficulty == "a":
        guess_limit = 3
    elif difficulty == "d":
        guess_limit = 1
    elif difficulty == "admin":
        admin_control += 1
        guess_limit = 99999999999999999
    else:
     user_score = 0
     print("Your score is " + str(user_score))

def admin(username):
    print("Admin Room")


def end(user_score):
    print("Thanks for playing " + username)
    print("Here is your final score. " + str(user_score))
    sys.exit()

def level18(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("level 18")
    print("Your score is " + str(user_score))
    secret_word = "boobies"
    print("Here is a clue.\nThe woman's body part that produce milk. It is boobi__\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wront guess, you got " + str(guess_limit - guess_count) + " guesses left!")
        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            leve18(user_score, guess_limit)

    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level17(user_score, guess_limit)
def level17(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 17")
    print("Your score is " + str(user_score))
    secret_word = "taxes"
    print("Here is a clue.\nThere is nothing more certain than death and _____.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wront guess, you got " + str(guess_limit - guess_count) + " guesses left!")
        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level18(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            leve18(user_score, guess_limit)

    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level17(user_score, guess_limit)

def level16(user_score,guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 16")
    print("Your score is " + str(user_score))
    secret_word = "earth"
    print("Here is a clue.\nWhere we all live.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")
        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level17(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level17(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level17(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level17(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            leve16(user_score, guess_limit)

    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level16(user_score, guess_limit)


def level15(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 15")
    print("Your score is " + str(user_score))
    secret_word = "earth"
    print("Here is a clue.\nWhere we all live.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")
        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level16(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level16(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level16(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level16(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            leve15(user_score, guess_limit)

    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level15(user_score, guess_limit)

def level14(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 14")
    print("Your score is " + str(user_score))
    secret_word = "mandarin chinese"
    print("Here is a clue.\nMost spoken first language.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")
        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level15(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level15(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level15(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)

    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level14(user_score, guess_limit)
def level13(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 13")
    print("Your score is " + str(user_score))
    secret_word = "jupiter"
    print("Here is a clue.\nBiggest planet in out solar system.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level14(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level13(user_score, guess_limit)
def level12(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 12")
    print("Your score is " + str(user_score))
    secret_word = "blue whale"
    print("Here is a clue.\nOne of the largest species in the planet earth we currently know.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level13(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level13(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level13(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level13(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level13(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level12(user_score, guess_limit)
def level11(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 11")
    print("Your score is " + str(user_score))
    secret_word = "google"
    print("In couple of the further levels, there will be no list and the only thing to guess the answer is the clue given.")
    print("Here is a clue.\nMost used search engine.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level12(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level12(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level12(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level12(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level12(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level11(user_score, guess_limit)
def level10(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 10")
    print("Your score is " + str(user_score))
    secret_word_list = ["New York", "Mumbai", "Mexixo City", "Tokyo", "Beijing", "Berlin", "London", "Moscow","Miami", "Mandrid", "Manila"]
    secret_word = "Tokyo"
    print(secret_word_list)
    print("Here is a clue.\nI am known as the eastern capital.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level11(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level11(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level11(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level11(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level11(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level10(user_score, guess_limit)
def level9(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 9")
    print("Your score is " + str(user_score))
    secret_word_list = ["embryon", "microphage", "dentritic cell", "neuron", "T cells", "liver", "spermatozoa", "brain", "Liverpool", "bacteriophage"]
    secret_word = "embryon"
    print(secret_word_list)
    print("Here is a clue.\nBiggest cell in a human body.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level10(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level10(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level10(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level10(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level10(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level9(user_score, guess_limit)
def level8(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 8")
    print("Your score is " + str(user_score))
    secret_word_list = ["Canada", "Germany", "Dubai", "Russia", "France", "Burkina Faso", "Ivory Coast", "Nambia", "Suriname", "El Salvador"]
    secret_word = "Dubai"
    print(secret_word_list)
    print("Here is a clue.\nI am not a country.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level9(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level9(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level9(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level9(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level9(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level8(user_score, guess_limit)
def level7(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 7")
    print("Your score is " + str(user_score))
    secret_word_list = ["Germany", "Burundi", "Andorra", "Lesotho", "El Salvador", "Slovakia", "Egypt", "Iraq", "Swaziland", "Mozambique"]
    secret_word = "Iraq"
    print(secret_word_list)
    print("Here is a clue.\nI am in Asia.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level8(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level8(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level8(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level8(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level8(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level7(user_score, guess_limit)
def level6(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 6")
    print("Your score is " + str(user_score))
    secret_word_list = ["69", "58", "12", "11", "69435", "31", "78","96", "876", "348"]
    secret_word = "69"
    print(secret_word_list)
    print("Here is a clue.\nFind the funniest number.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level7(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level7(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level7(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level7(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level7(user_score, guess_limit)
    else:
        print("You lose. " + username + ".")
        user_score -= 100
        print(str(user_score))
        if difficulty == "d":
            end(user_score)
        else:
            level6(user_score, guess_limit)
def level5(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 5")
    print("Your score is " + str(user_score))
    secret_word_list = ["Berlin", "Paris", "London", "Beijing", "New Dehli", "New York", "Vatican City", "Moscow", "Tokyo", "Tehran"]
    secret_word = "New York", "new york", "New york"
    print(secret_word_list)
    print("Here is a clue.\nFind the odd capital.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level6(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level6(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level6(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level6(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level6(user_score, guess_limit)
        else:
            print("You lose. " + username + ".")
            user_score -= 100
            print(str(user_score))
            if difficulty == "d":
                end(user_score)
            else:
                level5(user_score, guess_limit)
def level4(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 4")
    print("Your score is " + str(user_score))
    secret_word_list = ["smartphone", "laptop", "monitor", "keyboard", "mouse", "wire", "mousepad", "clock", "power button", "electricity"]
    secret_word = "mouse"
    print(secret_word_list)
    print("Here is a clue.\nIt could either be an animal or part of a computer setup.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level5(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level5(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level5(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level5(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level5(user_score, guess_limit)
        else:
            print("You lose. " + username + ".")
            user_score -= 100
            print(str(user_score))
            if difficulty == "d":
                end(user_score)
            else:
                level4(user_score, guess_limit)


def level3(user_score, guess_limit):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 3")
    print("Your score is " + str(user_score))
    secret_word_list = ["monster", "ghost", "rice", "milk", "ball", "light", "pencil", "box", "ruler", "marker"]
    secret_word = "ghost"
    print(secret_word_list)
    print("Here is a clue.\nIt huant you in your sleep and scare other people. His name is casper.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level4(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level4(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level4(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level4(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level4(user_score, guess_limit)
        else:
            print("You lose. " + username + ".")
            user_score -= 100
            print(str(user_score))
            if difficulty == "d":
                end(user_score)
            else:
                level3(user_score, guess_limit)
def level2(user_score, guess_limit, admin_control):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 2")
    print("Your score is " + str(user_score))
    secret_word_list = ["monster", "ship", "galaxy", "house", "television", "cup", "binder", "key", "paper", "ladder"]
    secret_word = "galaxy"
    print(secret_word_list)
    print("Here is a clue.\nWe call it the milky way.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level3(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level3(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level3(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level3(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level3(user_score, guess_limit)
        else:
            print("You lose. " + username + ".")
            user_score -= 100
            print(str(user_score))
            if difficulty == "d":
                end(user_score)
            else:
                level2(user_score, guess_limit)
def level1(user_score, guess_limit, admin_control):
    guess = 0
    guess_count = 0
    out_of_guesses = False
    print("Level 1")
    print("Your score is " + str(user_score))
    secret_word_list = ["car", "plane", "giraffe", "food", "toy", "smartphone", "bottle", "laptop", "elephant",
                        "blanket"]
    secret_word = "elephant"
    print(secret_word_list)
    print("Here is a clue.\nIt is one of the biggest animal on land.\nYou can also end by typing 'end'")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess == "end":
                end(user_score)
            elif guess != secret_word:
                print("Wrong guess. You got " + str(guess_limit - guess_count) + " guesses left!")

        else:
            out_of_guesses = True

    if not (out_of_guesses):
        print("You win! " + username + ".")
        if guess_count == 1:
            user_score += 100
            print("Your new score is " + str(user_score))
            level2(user_score, guess_limit)
        elif guess_count == 2:
            user_score += 75
            print("Your new score is " + str(user_score))
            level2(user_score, guess_limit)
        elif guess_count == 3:
            user_score += 50
            print("Your new score is " + str(user_score))
            level2(user_score, guess_limit)
        elif guess_count == 4:
            user_score += 25
            print("Your new score is " + str(user_score))
            level2(user_score, guess_limit)
        elif guess_count == 5:
            user_score += 0
            print("Your new score is " + str(user_score))
            level2(user_score, guess_limit)
        else:
            print("You lose. " + username + ".")
            user_score -= 100
            print(str(user_score))
            if difficulty == "d":
                end(user_score)
            else:
                level1(user_score, guess_limit)
level1(user_score, guess_limit, admin_control)

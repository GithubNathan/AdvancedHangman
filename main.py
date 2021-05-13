import random

wordlist = ['malarkey', 'kraken', 'antebellum', 'organization', 'patience']

def Hangman():
    word = random.choice(wordlist)

    print("Welcome to hangman! The length of your word is " + str(len(word)) + " characters!")

    def FLGuess():

        print("Guess the first letter: ")
        firstletter = word[0]
        firstletterguess = input()

        if firstletterguess == firstletter:
            print("You got it! Guess the second character now: ")
            SLGuess()

        else:
            print("You're close! Try again.")
            FLGuess()

    def SLGuess():

        print("Guess the second letter: ")
        secondletterguess = input()
        secondletter = word[1]

        if secondletterguess == secondletter:

            print("Nice! Guess the third letter now!")
            TLGuess()

        else:
            print("So close! Try again.")
            SLGuess()

    def TLGuess():
        print("Guess the third letter: ")
        thirdletterguess = input()
        thirdletter = word[2]

        if thirdletterguess == thirdletter:
            print("You got it! Would you like to guess the full word? Y or N.")
            yesorno = input()

            if yesorno == "Y":

                fullwordguess()

            else:

                fourthletterguess()

        else:
            print("Close! Try again.")
            TLGuess()

    def fullwordguess():
        print("Guess the full word!")
        fullwordguess = input()

        if fullwordguess == word:
            print("You got the word! Play again? Y or N")
            playagain = input()

            if playagain == "Y":
                Hangman()

        else:

            print("That was not the right word. Guess again.")
            fullwordguess()

    def fourthletterguess():
        print("Guess the fourth letter!")
        fourthletterguess = input()
        fourthletter = word[3]

        if fourthletterguess == fourthletter:
            print("You got it! Guess the full word now.")
            fullwordguess()

        else:
            print("That was not the right letter. Guess again.")
            fourthletterguess()




    FLGuess()


Hangman()
#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     w0500154
#Student Name:  Joseph Petrash

# INPUT -------------------------------------------
# ask user for phrase to redact from
def getPhrase():
    phrase = input("Type a phrase (or quit to exit program): ")
    return phrase

# ask user for letters to radact
def getBadLetters():
    badLetters = input("Type a comma-separated list of letters to redact: ")
    # remove commas and spaces from the list
    #  so that it contains only letters
    badLetters = badLetters.replace(",", "")
    badLetters = badLetters.replace(", ", "")
    badLetters = badLetters.replace(" ", "")
    return badLetters

# PROCESS ---------------------------------------------
# compare each letter in each string and 
#   remove instances where they match
def checkPhrase(phrase, badLetters):
    # keep track of how many letters are removed
    count = 0
    # go through every letter in phrase
    for letter in phrase:
        # go through ever letter to be redacted
        for badLetter in badLetters:
            # if they are the same
            if letter == badLetter:
                # replace both the upper and lowercase
                #  letter with an underscore
                phrase = phrase.replace(letter.upper(), "_")
                phrase = phrase.replace(letter.lower(), "_")
                count += 1
    return phrase, count

# OUPUT -------------------------------------------------
# output string to the user
def outputPhrase(phrase, count):
    print("Number of letters removed {0}".format(count))
    print(phrase)

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # loop forever
    while True:
        # ask for phrase
        phrase = getPhrase()
        # if user enters exit, exit the loop
        if phrase == "exit":
            print("Closing program...")
            return
        # ask for bad letters
        badLetters = getBadLetters()
        # remove letters from phrase and return how 
        #   many letters were removed
        phrase, count = checkPhrase(phrase, badLetters)
        #output to the user
        outputPhrase(phrase, count)

    # YOUR CODE ENDS HERE

main()
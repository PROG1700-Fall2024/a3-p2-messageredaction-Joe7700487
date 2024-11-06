#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     w0500154
#Student Name:  Joseph Petrash



def getInput(phrase, badLetters):
    phrase = input("Type a phrase (or quit to exit program): ")
    badLetters = input("Type a comma-separated list of letters to redact: ")
    phrase = createList(phrase)
    badLetters = createList(badLetters)
    return phrase, badLetters

def createList(phrase):
    letters = []
    for i in phrase:
        letters.append(i)
    return letters

def checkForLetters(stringList, badList):
    for i in stringList:
        for j in badList:
            print(i, j)
            if i == j:
                stringList.remove(j)
    return stringList

def removeLetter(stringList, badLetter):
    pass

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    phrase = ""
    badLetters = ""
    phrase, badLetters = getInput(phrase, badLetters)
    redacted = checkForLetters(phrase, badLetters)
    print(redacted)

    # YOUR CODE ENDS HERE

main()
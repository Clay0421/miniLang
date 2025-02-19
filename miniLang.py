def menu():
    print("1. Translate")
    print("2. Leave")
    userInput=str(input("Choice: "))
    while userInput != "2":
        if userInput == "1":
            userLang = input("\n Language to translate from (2 to quit): ")
            if userLang == "2":
                print("Bye!")
                break
            otherLang = input("Language to translate to (2 to quit): ")
            if otherLang == "2":
                print("Bye!")
                break
            statement = input("Enter a sentence with no punctuation. \
miniLang is very small so use simple words with no \
accent markers. Some words are not be included \
and thus will be ignored. (2 to quit): ")
            if statement == "2":
                print("Bye!")
                break
            miniLang(userLang, otherLang, statement)
        elif userInput == 2:
            fileOpen
            return print("Good Bye")
        else:
            print("Not valid input ")
            break

def fileOpener(langHold, languages, files, userArray, otherArray):
    for x in range(len(languages)):
        #file = open(files[x], 'r')
        #print(file)
        if langHold[0] == languages[x]:
            for word in open(files[x], 'r'):
                userArray.append(word.strip().lower())
                
        elif langHold[1] == languages[x]:
            for word in open(files[x], 'r'):
                otherArray.append(word.strip().lower())
                
        else:
            print("Searching")
        
    #for file in files:
     #   file.close
def miniLang(myLang, otherLang, message):
    languages = ["English", "Spanish", "French", "German"]
    for x in range(len(languages)):
        if myLang.lower().strip() == languages[x].lower():
            myLang = languages[x]
            print("You have chosen "+languages[x]+".")
        if otherLang.lower().strip() == languages[x].lower():
            otherLang = languages[x]
            print("You have chosen "+languages[x]+".")

    langHold = [myLang, otherLang]
    userArray = []
    otherArray = []
    
    files = ["listOfWords.txt", "listOfWordsSp.txt", \
             "listOfWordsFr.txt", "listOfWordsGn.txt"]
    #print("Yes")
    fileOpener(langHold, languages, files, userArray, otherArray)
 
    messageArray = message.split()
    translateArray = []
    print(messageArray)
    checker = 0
    for word in userArray:
        #print("word: "+str(word))
        #for word in userArray:
        for x in messageArray:
            #print(word)
            if word == x.lower():
                translateArray.append(otherArray[checker])
                print(checker)
        checker += 1
    #print("Translation", translateArray)
    for i in translateArray:
        print(i, end=" ")
    return files

menu()


"""
    while message != "2":
        #message = 
        messageArray.append(message)
        if message == "X":
            messageArray.rstrip()
            message.rstrip()
        for index in range(len(userArray)):
            if message == userArray[index]:
                trArray.append(otherArray[index])
                print(trArray[index], end=" ")
"""
    


"""
    done = False
    while True:
        for index in messageArray:
            if index == "2" or messageArray[:] != userArray:
                #second condition could be problem messageArray[:]...
                print("Done")
                done = True
                break
        if done == True:
            break
"""
"""
    
miniLang("EnglisH", "SPanish ", str(input("Enter a word enter 'X' to remove a word: ")))

print("Done")


"""
"""
    for lang in langHold:
        if lang == "English":
            if lang == myLang:
                for word in fileEn:
                    userArray.append(word.strip())
                    #print("1"+word)
            else:
                for word in fileEn:
                    otherArray.append(word.strip())
                    #print(word)
        if lang == "Spanish":
            if lang == myLang:
                for word in fileSp:
                    userArray.append(word.strip())
                    #print("1"+word)
            else:
                for word in fileSp:
                    otherArray.append(word.strip())
                    #print(word)
        if lang == "French":
            if lang == myLang:
                for word in fileFr:
                    userArray.append(word.strip())
                    #print("1"+word)
            else:
                for word in fileFr:
                    otherArray.append(word.strip())
                    #print(word)
        if lang == "German":
            if lang == myLang:
                for word in fileGn:
                    userArray.append(word.strip())
                    #print("1"+word)
            else:
                for word in fileGn:
                    otherArray.append(word.strip())
                    #print(word)
"""


"""

    for lang in langHold:
        if lang == myLang:
            wordAppend(lang, file)

           
    for lang in langHold:
        if lang == "English":
            for word in fileEn:
                userArray.append(word)
                print(word)
        if lang == "Spanish":
            for word in fileSp:
                userArray.append(word)
                print(word)
        if lang == "French":
            for word in fileFr:
                userArray.append(word)
                print(word)
        if lang == "German":
            for word in fileGn:
"""
#chose a language you want to translate from

#chose language to translate to
# I am like happy sad everything go was no yes maybe food you


#pulls all the data from the particular page for their lang and lines up with chosen lang
#data pulled is store in array and user provides input and the word is pulled

#can remove words use an array to hold users input

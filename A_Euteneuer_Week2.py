

"""getInput() is a function the gets the users input (language choice) and returns a greeting in the selected language"""

def getInput():
    userInput = input("Hello! Please choose a greeting from one of the following languages: Japenese, Bahamian or Spanish.")

    """ I am using "or" incase the user capitalizes the language"""
    
    if userInput == "japanese" or userInput == "Japanese":
        print("こんにちは、元気ですか？")
    elif userInput == "bahamian" or userInput == "Bahamian":
        print("Had go bui?")
    elif userInput == "spanish" or userInput == "Spanish":
        print("Hola como estas?")
    else:
        print("Please choose one of the three languages")
        getInput()
        
                      
                     
getInput();


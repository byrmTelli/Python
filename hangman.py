import random

def displayStatus(hp):
    status=[
         """
    Status:
        ______
        |    |
        |          
        |
        |
        |
    ____=____
    
    """,
    """
    Status:
        ______
        |    |
        |    O      
        |
        |
        |
    ____=____
    
    """,
    """
    Status:
        ______
        |    |
        |    O      
        | ---|
        |    |
        |
    ____=____
    
    """,
    """
    Status:
        ______
        |    |
        |    O      
        | ---|---
        |    |
        |
    ____=____
    
    """,
    """
    Status:
        ______
        |    |
        |    O      
        | ---|---
        |    |
        |   [  
    ____=____
    
    """,
    """
    Status:
        ______
        |    |
        |    O      
        | ---|---           You Lose!
        |    |
        |   [ ]
    ____=____
    """
]
    
    print(status[hp])

def guess_result(vall):
    success=[
        """
        
            CORRECT!
        
        """,
        """
        
            WRONG!
        
        """
    ]   
    print(success[vall])

def guess_itter(correctWord):
    hiddenWord="_"*len(correctWord)
    guessed_words=[]
    try_chance=0
    while try_chance<5:
        if hiddenWord.__contains__("_")==False:
            print("Congrtz!!!")
            break


        guess=input("Take a guess:").lower()

        #aynı tahminler tekrarlanırsa:
        if guessed_words.__contains__(guess)==True:
            print("You already guessed this.")
        else:
            guessed_words.append(guess)
            print("Your guesses: "+ str(guessed_words))
            if guess==correctWord:
                hiddenWord=guess

            #eğer aranan karakter var ise:
            elif correctWord.__contains__(guess):
                #tamamen bilindiğinde           
                    
                for i in range(len(correctWord)):
                    if correctWord[i]==guess.lower():
                        hiddenWord=hiddenWord[:i]+guess+hiddenWord[i+1:]
                print(hiddenWord.upper())
                guess_result(0)
                displayStatus(try_chance)
                
                            
                
                #aranan karakter yok ise:
            else:
                print(hiddenWord.upper())
                try_chance=try_chance+1
                guess_result(1)
                displayStatus(try_chance)
    



wordlist=["network","payload","port","hardware","python","nmap","web","docker","facebook","github"] 
correctWord=random.choice(wordlist)
    
guess_itter(correctWord)
end=input("Good By!")
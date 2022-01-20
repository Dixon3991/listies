import time
import random

def playRound(seconds=10):
    """ Get user input repeatedly until timer runs out """
    start_time = time.time()
    notepad=[]
    while True:
        word = input("word: ")
        notepad.append(word)
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        if elapsed_time > seconds or len(notepad)==10:

            break
    
    return notepad

        
def bonusLetter():
    """ Pull Bonus Letter Card(s) at the start of the game """
    letters=['A', 'A', 'B', 'C', 'F', 'H', 'M', 'O', 'P', 'R', 'S', 'T', 'T', 'W']
    # TO DO: Incorporate "Group Choice"
    gc='Group Choice'
    # TO DO: Test Odds for Letter Choices
    return random.choices(letters, k=4)

def retrieveCategories():
    # TO DO: Categories file needs to be made (json)
    # TO DO: Open, Retrive, and Reformat Categories 
    # TO DO: Pass categories to pullCategories function
    pass

def pullCategory():
    """ Pull Category Card(s) at the start of the game """
    # TO DO: 
    categories = ["things that are cold", "things your boss naha you about", "things in the kitchen", "things you do when you are sad"]
    # TO DO: Test Odds for Categories 
    # Should NOT use the same category twice in One Game
    return random.choices(categories, k=4)

def fullGame():
    # TO DO: Revise fullGame()
    """ One Game is 4 Rounds """
    """ Pull Category Card before Round(s) begin """
    """ Pull Bonus Letter Card(s) before Round(s) begin """
    """ Begin Timed User Input """  
    r1 = playRound()

def rollDice():
    """ Roll the dice to get the bonus modifier """
    modifier=["EW", "WTF", "HOT", "OMG", "TRASHY", "BASIC"]
    random.shuffle(modifier)
    return random.choice(modifier)

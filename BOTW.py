
from time import sleep
import sys


def sprint(txt):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    print()


def slowprint(txt):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.03)
    print()


# Default player statistics ########################################################################################


gainedHeartContainers = 0
maxHealth = 3 + gainedHeartContainers
damageTaken = 0
totalHearts = maxHealth - damageTaken
healthDisplay = "♡" * totalHearts
playerCoordinateX = 0
playerCoordinateY = 0

playerHealthStats = [gainedHeartContainers, maxHealth, damageTaken, totalHearts, healthDisplay]
playerLocationStats = [playerCoordinateX, playerCoordinateY]

# MAIN GAME ########################################################################################################

print(""".---.                   .-. .-.            .--.   .-. .-.           .-.   .-. _ .-.     .-.
: .; :                 .' `.: :           : .-'  .' `.: :           : :.-.: ::_;: :     : :
:   .'.--.  .--.  .--. `. .': `-.    .--. : `;   `. .': `-.  .--.   : :: :: :.-.: :   .-' :
: .; :: ..'' '_.'' .; ; : : : .. :  ' .; :: :     : : : .. :' '_.'  : `' `' ;: :: :_ ' .; :
:___.':_;  `.__.'`.__,_;:_; :_;:_;  `.__.':_;     :_; :_;:_;`.__.'   `.,`.,' :_;`.__;`.__.'
""")
sprint("Welcome to Breath of the Wild: Text-Based Edition.")

sprint("This is a proof of concept game, which may or may not be finished as time goes on.")

sprint("The goal of the project is to include as much of BOTW's story and gameplay as possible, while taking its own "
       "spin on the game from time to time.")
sprint("The game will include things outside of BOTW's narrative, in the form of easter-eggs and/or additional "
       "narration for performing certain tasks a certain way/a certain amount of times.")


# '>>>' represents a choice to make and/or a prompt to perform an action
# '!>' represents an action you performed
# '?>' represents a comment from the game narrator

# Game Start Prompt ------------------------------------------------------------------------------------------------

answer = input(">>> Start New Game? (y/n)").lower().strip()
if answer == "n":
    print("################")
    slowprint("See you later...")
elif answer == "y":

    # Loop 1 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    asleep = True
    laziness = 0

    # Loop 1 START =================================================================================================

    while asleep:
        if laziness == 0:
            sprint("################################################################################################"
                   "######")
            slowprint("You hear a voice call out to you... It is barely audible, but you can hear it saying 'open "
                      "your eyes'.")
        elif laziness >= 1:
            slowprint("The voice once again calls out to you to open your eyes.")

        # Prompt 1-A START -----------------------------------------------------------------------------------------

        answer = input(">>> Open your eyes? (y/n)").lower().strip()
        if answer == "y":
            if laziness < 3:
                print("/**********************\\")
                slowprint("!> You open your eyes...")
                print("\\**********************/")
            elif laziness >= 3:
                print("/***************************************************\\")
                slowprint("!> You open your eyes...only took you 10,000 years...")
                print("\\***************************************************/")
            asleep = False
        elif answer == "n":
            laziness += 1  # Increase laziness
            if laziness < 3:
                print("/***********************\\")
                slowprint("!> You refuse the call...")
                print("\\***********************/")
            if laziness >= 3:
                print("/********************************************\\")
                slowprint("!> You refuse the call...")
                slowprint("?> You seem to be considering just dying here.")
                print("\\********************************************/")
        else:
            print("audible screeching")

        # Prompt 1-A END -------------------------------------------------------------------------------------------
    # Loop 1 END ===================================================================================================

    sprint("######################################################################################################")
    slowprint("You awake to a blinding blue light.")
    slowprint("As you gain focus, you find it is not one light, but an elaborate organic pattern of lights above you.")
    slowprint("You find yourself in a textured stone tub, filled with strange neon blue fluid.")
    slowprint("You hear a quiet rushing sound as the fluid slowly drains away.")
    sprint("######################################################################################################")

    # Loop 2 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    layingDown = True
    laziness = 0

    # Loop 2 START =================================================================================================

    while layingDown:

        # Prompt 2-A START -----------------------------------------------------------------------------------------

        answer = input(">>> Sit up? (y/n)").lower().strip()
        if answer == "y" or "yes":
            if laziness < 3:
                print("/**************\\")
                slowprint("!> You sit up...")
                print("\\**************/")
            elif laziness >= 3:
                print("/*************************************\\")
                slowprint("!> You sit up...")
                slowprint("?> Took you long enough...")
                print("\\*************************************/")
            layingDown = False
        elif answer == "n" or "no":
            laziness += 1
            if laziness < 3:
                print("/***************************************************************************\\")
                slowprint("!> You decide moving takes a bit too much from your effort budget right now...")
                print("\\****************************************************************************/")
            elif laziness >= 3:
                print("/**********************************************\\")
                slowprint("?> You seem to desire laying there for eternity.")
                print("\\**********************************************/")

        # Prompt 2-A END -------------------------------------------------------------------------------------------
    # Loop 2 END ===================================================================================================
    answer = input("Press Enter to Exit")
# If the player types anything other than y or n at the 'New Game' prompt:
else:
    print("I am error")

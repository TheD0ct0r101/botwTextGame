
from time import sleep
import sys
import os
from playsound import playsound
from game.World import *

# Non-dependant sound directory setup ##################################################################################

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
prompt_continue = os.path.join(root_dir, "assets", "prompt_continue.wav")

# Fancy text scrolling #################################################################################################


def sprint(txt):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.005)
    print()


def slowPrint(txt):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.03)
    print()


# Default player statistics ############################################################################################


gainedHeartContainers = 0
maxHealth = 3 + gainedHeartContainers
damageTaken = 0
totalHearts = maxHealth - damageTaken
healthDisplay = "♡" * totalHearts
playerLocationWorld = worldLocation(0.0)
playerLocationRoom = worldLocationRoom(0)

playerHealthStats = [gainedHeartContainers, maxHealth, damageTaken, totalHearts, healthDisplay]

# MAIN GAME ############################################################################################################

print(""".---.                   .-. .-.            .--.   .-. .-.           .-.   .-. _ .-.     .-.
: .; :                 .' `.: :           : .-'  .' `.: :           : :.-.: ::_;: :     : :
:   .'.--.  .--.  .--. `. .': `-.    .--. : `;   `. .': `-.  .--.   : :: :: :.-.: :   .-' :
: .; :: ..'' '_.'' .; ; : : : .. :  ' .; :: :     : : : .. :' '_.'  : `' `' ;: :: :_ ' .; :
:___.':_;  `.__.'`.__,_;:_; :_;:_;  `.__.':_;     :_; :_;:_;`.__.'   `.,`.,' :_;`.__;`.__.'
VERSION: Alpha 1.0.0""")

sprint("""Welcome to Breath of the Wild: Text-Based Edition.

This is a proof of concept game, which may or may not be finished as time goes on.

The goal: include as much of BOTW's story and gameplay as possible, 
while taking its own spin on the game from time to time.

The game will include things outside of BOTW's narrative, in the form of easter-eggs
and/or additional narration for performing certain tasks a certain way/a certain amount of times.
""")


# '>>>' represents a choice to make and/or a prompt to perform an action
# '!>' represents an action you performed
# '?>' represents a comment from the game narrator

# Game Start Prompt ----------------------------------------------------------------------------------------------------

answer = input(">>> Start New Game? (y/n)").lower().strip()
if answer == "n" or answer == "no":
    playsound(prompt_continue)
    sprint("################")
    slowPrint("See you later...")
    answer = input("Press Enter to Exit")
elif answer == "y" or answer == "yes":
    playsound(prompt_continue)

    # Loop 1 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    asleep = True
    laziness = 0

    # Loop 1 START =====================================================================================================

    while asleep:
        if laziness == 0:
            sprint("################################################################################################"
                   "######")
            slowPrint("You hear a voice call out to you... It is barely audible, but you can hear it saying 'open "
                      "your eyes'.")
        elif laziness >= 1:
            slowPrint("The voice once again calls out to you to open your eyes.")

        # Prompt 1-A START ---------------------------------------------------------------------------------------------

        answer = input(">>> Open your eyes? (y/n)").lower().strip()
        if answer == "y" or answer == "yes":
            playsound(prompt_continue)
            if laziness < 3:
                print("/**********************\\")
                slowPrint("!> You open your eyes...")
                print("\\**********************/")
                sleep(0.3)
            elif laziness >= 3:
                print("/***************************************************\\")
                slowPrint("!> You open your eyes...only took you 10,000 years...")
                print("\\***************************************************/")
                sleep(0.3)
            asleep = False
        elif answer == "n" or answer == "no":
            playsound(prompt_continue)
            laziness += 1  # Increase laziness
            if laziness < 3:
                print("/***********************\\")
                slowPrint("!> You refuse the call...")
                print("\\***********************/")
                sleep(0.3)
            if laziness >= 3:
                print("/********************************************\\")
                slowPrint("""!> You refuse the call...
?> You seem to be considering just dying here.""")
                print("\\********************************************/")
                sleep(0.3)
        else:
            playsound(prompt_continue)
            print("audible screeching")

        # Prompt 1-A END -----------------------------------------------------------------------------------------------
    # Loop 1 END =======================================================================================================

    sprint("######################################################################################################")
    slowPrint("""You awake to a blinding blue light.
As you gain focus, you find it is not one light, but an elaborate organic pattern of lights above you.
You find yourself in a textured stone tub, filled with strange neon blue fluid.
You hear a quiet rushing sound as the fluid slowly drains away.""")
    sprint("######################################################################################################")

    # Loop 2 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    layingDown = True
    laziness = 0

    # Loop 2 START =====================================================================================================

    while layingDown:

        # Prompt 2-A START ---------------------------------------------------------------------------------------------

        answer = input(">>> Sit up? (y/n)").lower().strip()
        if answer == "y" or answer == "yes":
            playsound(prompt_continue)
            if laziness < 3:
                print("/**************\\")
                slowPrint("!> You sit up...")
                print("\\**************/")
            elif laziness >= 3:
                print("/*************************************\\")
                slowPrint("!> You sit up...")
                slowPrint("?> Took you long enough...")
                print("\\*************************************/")
            layingDown = False
        elif answer == "n" or answer == "no":
            playsound(prompt_continue)
            laziness += 1
            if laziness < 3:
                print("/***************************************************************************\\")
                slowPrint("!> You decide moving takes a bit too much from your effort budget right now...")
                print("\\****************************************************************************/")
            elif laziness >= 3:
                print("/**********************************************\\")
                slowPrint("?> You seem to desire laying there for eternity.")
                print("\\**********************************************/")
        else:
            playsound(prompt_continue)
            print("You have one job.")

        # Prompt 2-A END -----------------------------------------------------------------------------------------------
    # Loop 2 END =======================================================================================================
    answer = input("Press Enter to Exit")
# If the player types anything other than y or n at the 'New Game' prompt:
else:
    playsound(prompt_continue)
    print("I am error")

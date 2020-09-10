
class Game:

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
    
    Welcome to Breath of the Wild: Text-Based Edition.
    
    This is a proof of concept game, which may or may not be finished as time goes on.
    """)

    # '>>>' represents a choice to make and/or a prompt to perform an action
    # '!>' represents an action you performed
    # '?>' represents a comment from the game narrator

    # Game Start Prompt ------------------------------------------------------------------------------------------------

    answer = input(">>> Start New Game? (y/n)").lower().strip()
    if answer == "n":
        print("################")
        print("See you later...")
    elif answer == "y":

        # Loop 1 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        asleep = True
        laziness = 0

        # Loop 1 START =================================================================================================

        while asleep:
            if laziness == 0:
                print("################################################################################################"
                      "######")
                print("You hear a voice call out to you... It is barely audible, but you can hear it saying 'open "
                      "your eyes'.")
            elif laziness >= 1:
                print("The voice once again calls out to you to open your eyes.")

            # Prompt 1-A START -----------------------------------------------------------------------------------------

            answer = input(">>> Open your eyes? (y/n)").lower().strip()
            if answer == "y":
                if laziness < 3:
                    print("/**********************\\")
                    print("!> You open your eyes...")
                    print("\\**********************/")
                elif laziness >= 3:
                    print("/***************************************************\\")
                    print("!> You open your eyes...only took you 10,000 years...")
                    print("\\***************************************************/")
                asleep = False
            elif answer == "n":
                laziness += 1  # Increase laziness
                if laziness < 3:
                    print("/***********************\\")
                    print("!> You refuse the call...")
                    print("\\***********************/")
                if laziness >= 3:
                    print("/********************************************\\")
                    print("!> You refuse the call...")
                    print("?> You seem to be considering just dying here.")
                    print("\\********************************************/")
            else:
                print("audible screeching")

            # Prompt 1-A END -------------------------------------------------------------------------------------------
        # Loop 1 END ===================================================================================================

        print("######################################################################################################")
        print("You awake to a blinding blue light.")
        print("As you gain focus, you find it is not one light, but an elaborate organic pattern of lights above you.")
        print("You find yourself in a stone waterbed, filled with strange neon blue fluid.")
        print("You hear a quiet rushing sound as the fluid slowly drains away")
        print("######################################################################################################")

        # Loop 2 PREP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        layingDown = True
        laziness = 0

        # Loop 2 START =================================================================================================

        while layingDown:

            # Prompt 2-A START -----------------------------------------------------------------------------------------

            answer = input(">>> Sit up? (y/n)").lower().strip()
            if answer == "y":
                if laziness < 3:
                    print("/**************\\")
                    print("!> You sit up...")
                    print("\\**************/")
                elif laziness >= 3:
                    print("/*************************************\\")
                    print("!> You sit up...")
                    print("?> Took you long enough...")
                    print("\\*************************************/")
                layingDown = False
            elif answer == "n":
                laziness += 1
                if laziness < 3:
                    print("/***************************************************************************\\")
                    print("!> You decide moving takes a bit too much from your effort budget right now...")
                    print("\\****************************************************************************/")
                elif laziness >= 3:
                    print("/**********************************************\\")
                    print("?> You seem to desire laying there for eternity.")
                    print("\\**********************************************/")

            # Prompt 2-A END -------------------------------------------------------------------------------------------
        # Loop 2 END ===================================================================================================

    # If the player types anything other than y or n at the 'New Game' prompt:
    else:
        print("I am error")

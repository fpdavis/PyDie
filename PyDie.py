import random
import sys
import string

# This routine guarantees we always get an integer from a given string
# It does its best to remove any non integers
def intTryParse(sValue):
    try:
        # We want to keep the negative sign but remove all other non numeric characters
        sPunctuation = string.punctuation.replace("-","")
        sValue = sValue.translate(str.maketrans('', '', string.ascii_letters)).translate(str.maketrans('', '', sPunctuation))
        
        if (len(sValue) > 0):
            return int(sValue)
        else:
            return 0
    except ValueError:
        return 0
    
# Begin RollDie function
def RollDie( sMyInput ):

    sResults = ""
    iPlusModifier = 0
    iTotal = 0
    
    # Begin spliting up input string (i.e. 1D20+1)
    aData = sMyInput.split("D");
    
    if (len(aData) > 0):
       iNumberDie = intTryParse(aData[0])
       
       if (iNumberDie < 1):
            iNumberDie = 1 # Default value if none specified

    else:
        iNumberDie = 1 # Default value if none specified
    
    # We do all these len() checks in case the input is missing values
    # such as number of dice to roll, number of sides, or modifier
    if (len(aData) > 1 ):
        aRightOfDData = aData[1].split("+")
        iNumberSides = intTryParse(aRightOfDData[0])

        if (iNumberSides < 1):
            iNumberSides = 20 # Default value if none specified
            
        if (len(aRightOfDData) > 1):    
            iPlusModifier = intTryParse(aRightOfDData[1])
        else:
            iPlusModifier = 0 # Default value if none specified
    else:
        iNumberSides = 20 # Default value if none specified
    # End spliting up
    
    # Here we do the actual rolling and store the value for later        
    for i in range(0, iNumberDie):
        iResults = random.randint(1, int(iNumberSides))
        sResults += str(iResults) + ", "
        iTotal += iResults
    
    # Add the modifier to the final total
    iTotalWithBonus = iTotal + iPlusModifier
        
    # Do some formating of the final output for this set of rolls
    print("(D{0}) Rolls: ".format(iNumberSides) + sResults[:-2])
    
    if (iPlusModifier > 0):
        print("      Modifier: +" + str(iPlusModifier))
    
    print("      Total: " + str(iTotalWithBonus))

    return
# End RollDie Function

# Command Line Arguments (argv)
# To pass argv to a script in Spyder, you need to go the menu entry
#    Run > Configuration per file
# or press the Ctrl+F6 key, then look for the option called
#    Command line options

sMyInput = ""
#sMyInput = "1D20" # Uncomment this line for easy testing of values

bRepeat = False
 
if (len(sMyInput) == 0 and len(sys.argv) > 1):
    del sys.argv[0]
    sMyInput = ','.join(str(oEachElement) for oEachElement in sys.argv)
elif (len(sMyInput) == 0):
    bRepeat = True
    sMyInput = input("Input (4D8,D20,1d20+2,etc)?")

while True:
    if (len(sMyInput) == 0 or sMyInput.lower() == "exit"):
        break # No input was specified so we exit
    
    # Remove whitespace, capitalize the string, and then split it on commas (take the string and convert it to an array)
    aRolls = sMyInput.translate(str.maketrans('', '', string.whitespace)).upper().split(",")
    
    # Call teh RollDie routine for each element in the array that was split above
    [RollDie(sRoll) for sRoll in aRolls]
    
    if not bRepeat:
        break # We received a command line argv or test input so exit after one run
    
    sMyInput = input("Input (Enter to exit)?")

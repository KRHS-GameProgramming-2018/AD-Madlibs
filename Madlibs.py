from screens import *
from getInput import *
import story1
import story2
import story3


print showSplash()
raw_input("Press Enter to Start")

swearCount = [0];

go = True
while go:
    if swearCount[0] == 3:
        print showLockScreen
    else:
        print showMenu()
        response = getMenuInput()
        if response == "Q":    
            go = False
            print "Goodbye and thanks for playing"
        elif response == "1":
            print story1.playMadlibs(swearCount)
            raw_input("Press Enter to Continue")
        elif response == "2":
            print story2.playMadlibs(swearCount)
            raw_input("Press Enter to Continue")
        elif response == "3":
            print story3.playMadlibs(swearCount)
            raw_input("Press Enter to Continue")
        else:
            print "OMG Got invalid menu option!!!"


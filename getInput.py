def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "2" 
            or response == "Two"):
            response = "2"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True              
        else:
            print "Please make a valid choice"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word



def getPhone (prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isPhone(word):
            goodInput = True
        else:
            print "Haven't heard of that one"
    return word



def isPhone(word):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    phoneList = [ "android",
                "samsung",
                "iphone",
                "iphone",
                "lg",
                "google",
                "one plus",
                "galaxy",
                "note",
                "motorola",
                "nokia",
                "s",
                "x"
                ]
    words = word.split(" ")
    for w in words:
        if (w.lower() not in phoneList) and (w not in nums):
            return False
    return True
        
        


def getMountain(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isMountain(word):
            goodInput = True
        else:
            print "Mountain not recognised "
    return word                



def isMountain(word):
    MountainList = [ "kearsarge",
                    "sunapee",
                    "cannon",
                    "washington",
                    "jefferson",
    ]
    if word.lower() in MountainList:
        return True
    else:
        return False

def getDay(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isDay(word):
            goodInput = True
        else:
            print "Please enter a day of the week "
        return word




def isDay(word):
    dayList = [ "monday", 
               "tuesday",
               "wednesday",
               "thursday",
               "friday",
               "saturday",
               "sunday",
               ]
    if word.lower() in dayList:
        return True
    else:
        return False
               
    






def isSwear(word):
    swearList = ["crap",
                "piss",
                "shit",
                "bitch",
                "bitchy",
                "bastard",
                "fuck",
                "fuc",
                "fuq",
                "phuck",
                "phuc",
                "phuq",
                "fucked",
                "fucker",
                "nigger",
                "nigga",
                "negro",
                "damn",
                "pussy",
                "dick",
                "vagina",
                "penis",
                ]
    words = word.split(" ")
    for w in words:
        if w.lower() in swearList:
            return True
    return False



def getMeasure(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        goodInput = False
        if isMeasure(word):
            goodInput = True
        else:
            print "Please enter a unit of measure "
        return word


def isMeasure(word):
    measureList = ["pounds",
                   "lbs",
                   "ounces",
                   "oz",
                   "pints",
                   "liters",
                   "milliliters",
                   "kiloliters",
                   "gallons",
                   "cups",
                   ]
    if word.lower() in measureList:
        return True
    else:
        return False


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
        elif (response == "3" 
            or response == "three"):
            response = "3"
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




def getWord(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0] # Probably should turn this off once it works...or make it a message about how close they are to being in trouble
    return word




def getNumber(prompt, minNumber, maxNumber, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if isSwear(word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
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




def getPhone (prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear (word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
        if isPhone(word):
            goodInput = True
        elif not isSwear (word): # This is a little redundant; you could have just used else
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
        
        


def getMountain(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear (word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
        if isMountain(word):
            goodInput = True
        elif not isSwear(word):
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





def getDay(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear (word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
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
                "fucking",
                "fucked",
                "fuc",
                "fuq",
                "phuck",
                "phucking",
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




def getMeasure(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear(word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
        if isMeasure(word):
            goodInput = True
        elif not isSwear (word):
            print " please enter a unit of measurement"
            goodInput = False
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




def getNumber1(prompt, minNumber, maxNumber, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
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




def getWord2(prompt, sc = None): # how is this different then getWord
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            if sc: 
                sc[0] += 1
                print sc[0]
    
    return word




def getFruit(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
        if isFruit (word):
            goodInput = True
        else:
            goodInput = False
            print "Please enter a fruit "
    return word




def isFruit(word):
    fruitList = [ "strawberry", 
               "grape",
               "banana",
               "apple",
               "orange",
               "blueberry",
               "cherry",
               "peach",
               "cranberry",
               ]
    if word.lower() in fruitList:
        return True
    else:
        return False
               



def getSize(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            if sc: 
                sc[0] += 1
                print sc[0]
    return word




def getCarCompany(prompt, sc = None):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear (word):
            goodInput = False
            print "Watch your language!"
            if sc:
                sc[0] += 1
                print sc[0]
        if isCarCompany(word):
            goodInput = True
        elif not isSwear:
            print "Never heard of that car company"
    return word


    

def isCarCompany(word):
    carCompanyList = ["acura",
                    "aston",
                    "aston martin",
                    "audi",
                    "bentley",
                    "bmw",
                    "bugatti",
                    "chevrolet",
                    "chevy",
                    "chrystler",
                    "dodge",
                    "ferrari",
                    "fiat",
                    "ford",
                    "gmc",
                    "honda",
                    "hyundai",
                    "jag",
                    "jaguar",
                    "lambo",
                    "lamborghini",
                    "lexus",
                    "mini",
                    "nissan",
                    "pagani",
                    "subaru",
                    "mitsubishi",
                    "toyota",
                    "plymouth"
                    "oldsmobile",
                    "pontiac",
                    "porsche",
                    "vw",
                    "volkswagen",
                    "mercedes",
                    "saab",
                    "volvo",
                    ]
    if word.lower() in carCompanyList:
        return True
    else:
        return False  

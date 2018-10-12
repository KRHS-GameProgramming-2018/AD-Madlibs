from getInput import *

def playMadlibs():
    
    adjective = getWord ("Please enter an adjective: ")
    name1 = getWord ("please enter a name: ")
    carCompany = getCarCompany ("Please enter a car company: ")
    speed = getNumber ("Please enter a number: ", 60, 250)
    verb = getWord ("Please enter a verb: ")
    animal = getWord ("Please enter a plural animal: ")
    verb2 = getWord ("Please enter another verb: ")
    
    
    output = ""
    output += "Life can be " + adjective + "."
    output += " However, life isn't all " + adjective + "."
    output += " Just look at " + name1 + " driving their new " + carCompany + "."
    output += " Just watch as " + name1 + ", oh whats this? "
    output += name1 + " is going " + speed + " mph!"
    output += " Their going to " + verb + " all the " + animal + " in the road!"
    output += " Quick, " + verb2 + " away, " + verb2 + " away as fast as you can!"
    output += " Well, I guess life still can be " + adjective + ". Just not for everyone."
    

    return output

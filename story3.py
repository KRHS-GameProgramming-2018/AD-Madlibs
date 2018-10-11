from getInput import *

def playMadlibs():
    
    adjective = getWord ("Please enter an adjective: ")
    name = getWord ("please enter a name: ")
    carCompany = getCarCompany ("Please enter a car company: ")
    name = getWord ("Please enter a name: ")
    speed = getNumber ("Please enter a number: ", 60, 250)
    verb = getWord ("Please enter a verb: ")
    
        
    output += "Life can be " + adjective + "."
    output += "However, life isn't all " + adjective + "."
    output += "Just look at " + name + " driving their new " + carCompany + "."
    output += "Just watch as " + name + ", oh whats this?"
    output += name + " is going " + speed + " mph!"
    output += "Their going to mow down all the " + animal + " in the road!"
    output += "Quick, " + verb + " away, " + verb + " away as fast as you can!"
    output += "Well, I guess life still can be " + adjective + "."
    output += "Just not for everyone."
    

    return output

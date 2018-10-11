from getInput import *

def playMadlibs():
    
    adjective = getWord ("Please enter an adjective: ")
    name1 = getWord ("please enter a name: ")
    carCompany = getCarCompany ("Please enter a car company: ")
    name = getWord ("Please enter a name: ")
    speed = getNumber ("Please enter a number: ", 60, 250)
    animal = getWord ("Please enter an animal: ")
    verb = getWord ("Please enter a verb: ")
    
    
    output = ""
    output += "Life can be " + adjective + "."
    output += "However, life isn't all " + adjective + "."
    output += "Just look at " + name1 + " driving their new " + carCompany + "."
    output += "Just watch as " + name1 + ", oh whats this?"
    output += name1 + " is going " + speed + " mph!"
    output += "Their going to mow down all the " + animal + " in the road!"
    output += "Quick, " + verb + " away, " + verb + " away as fast as you can!"
    output += "Well, I guess life still can be " + adjective + ". Just not for everyone."
    

    return output

from getInput import *

def playMadlibs():
    
    adjective = getWord ("Please insert an adjective: ")
    name = getWord ("please insert a name: ")
    carCompany = getCarCompany ("Please insert a car company: ")
    
        
    output += "Life can be " + adjective + "."
    output += "However, life isn't all " + adjective + "."
    output += "Just look at " + name + " driving there new " + carCompany + "."
    

    return output

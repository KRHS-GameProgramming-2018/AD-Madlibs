from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    color1 = getWord("Enter a color: ")
    brandofphone = getWord("Enter phone brand: ")
    
    
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1
    output += " I turned and saw the animals my friend was talking about. To my suprise, they had " + color1 + " skin."
    output += " In my suprise, I pulled out my " +brandofphone + " and took a picture. "
    
    
    
    
    return output

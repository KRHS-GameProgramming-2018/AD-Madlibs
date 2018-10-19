from getInput import *

def playMadlibs(sc):
    friend1 = getWord("Enter a Name: ", sc)
    numAnimals = getNumber("Enter a number: ", 2, 10, sc)
    animals1 = getWord("Enter a pluaral animal name: ", sc)
    color1 = getWord("Enter a color: ", sc)
    bodyCover = getWord("Enter a body cover, fur, skin, scales etc: ", sc)
    phone = getPhone("Enter phone: ", sc)
    mountainInNH = getMountain ("Enter the name of a mountain in NH: ", sc)
    day =  getDay ("Name a day of the week: ", sc)
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1 
    output += " I turned and saw the animals my friend was talking about. To my suprise, they had " + color1 + " " + bodyCover + "."
    output += " In my suprise, I pulled out my " + phone + " and took a picture. "
    output += " The next day, I printed out the photos I had taken yesterday and to my suprise, they were empty."
    output += " The next day, I went to see my friend to ask them about the wierd animals we had seen yesterday."
    output += " Hey, do you remember the animals we saw yesterday while walking up mount " + mountainInNH + ". "
    output += " No, he responded. I took out my phone to show him the photo, to my suprise, the photo was deleted."
    output += " To this day, I was never sure if I had seen those wierd animals on that " + day + " afternoon. "
    
    
    
    
    
    return output

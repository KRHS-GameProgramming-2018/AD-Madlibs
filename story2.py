from getInput import *

def playMadlibs(sc):
 number1 = getNumber1 ("pick a number ", 0, 10, sc)
 color = getWord2 ("choose a color ", sc)
 unitsOfMeasure = getMeasure ("enter a unit of measurement ", sc) 
 number2 = getNumber ("pick another number ", 0, 10, sc)
 adverb = getWord ("enter a verb ", sc)
 size = getSize ("choose a size ie: large, small, huge, tiny: ", sc)
 fruit = getWord ("choose a fruit ", sc)
 pancakeTopping = getWord ("name a pancake toping ", sc)



 output = " Story by Derek "
 output += "As I got up this morning, I decided to make pancakes for breakfast."
 output += " First, I added " + number1 + " cups of flour."
 output += " Next came the " + color + " baking powder."
 output += " After mixing in the salt and sugar, I dumped in the 2 " + unitsOfMeasure + " of milk and"
 output += " I cracked one egg and added it in. Next, I added in " +number2 + " tablespoons of melted butter."
 output += " Heating up the griddle, I whisked the ingredients " + adverb + " until a batter was formed."
 output += " Next, I poured the batter into the scalding skillet and watched as " + size + " pancakes started forming."
 output += " A couple mintes later, I turned off the heat and sat down to eat my freshly made pancakes"
 output += " I dumped on some " + fruit + " and " + pancakeTopping + " and ate my breakfast. "



 return output 

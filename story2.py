from getInput import *

def playMadlibs():
 number1 = getNumber ("pick a number ", 0, 10)
 color = getWord ("choose a color ")
 unitsOfMeasure = getMeasure ("enter a unit of measurement ") 
 number2 = getNumber ("pick another number ", 0, 10)
 verb = getWord ("enter a verb ")
 size = getSize ("choose a size ie: large, small, huge, tiny ")
 fruit = getWord ("choose a fruit ")
 pancakeside = getWord ("name a pancake toping ")



 output += " Story by Derek "
 output += "As I got up this morning, I decided to make pancakes for breakfast. "
 output += " First, I added " + number1 + " cups of flour."
 output += "Next came the " + color + " baking powder."
 output += " After mixing in the salt and sugar, I dumped in the 2 " + unitsOfMeasure + " of milk "
 output += "I cracked one egg and added it in. Next, I added in " +number2 + "tablespoons of melted butter. "
 output += " Heating up the griddle,I whisked the ingredients " + verb + " until a batter was formed."
 outout += "Next, I poured the batter into the scalding skillet and watched as " + size + "pancakes started forming."
 output += " A couple mintes later, I turned off the heat and sat down to eat my freshly made pancakes"
 output += " I dumped on some" + fruit + " and " + pancakeside + " and ate my breakfast. "



 return output 

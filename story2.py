from getInput import *

def playMadlibs():
 number1 = getnumber ( pick a number)
 color = getcolor ( choose a color)
 unitsofmeasure = getmeasure ( enter a unit of measurement) 
 number2 = getnumber2 ( pick another number)
 verb = getverb ( enter a verb)
 size = getsize ( choose a size ie: large, small, huge, tiny)
 fruit = getfruit ( choose a fruit)
 pancakeside = getside (name a pancake toping)



 output += " Story by Derek "
 output += "As I got up this morning, I decided to make pancakes for breakfast. "
 output += " First, I added " + number1 + " cups of flour."
 output += "Next came the " + color + " baking powder."
 output += " After mixing in the salt and sugar, I dumped in the 2 " + unitsofmeasure + " of milk "
 output += "I cracked one egg and added it in. Next, I added in " +number2 + "tablespoons of melted butter. "
 output += " Heating up the griddle,I whisked the ingredients " + verb + " until a batter was formed."
 outout += "Next, I poured the batter into the scalding skillet and watched as " + size + "pancakes started forming."
 output += " A couple mintes later, I turned off the heat and sat down to eat my freshly made pancakes"
 output += " I dumped on some" + fruit + " and " + pancakeside + " and ate my breakfast. "



 return output 

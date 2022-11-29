#Emily Rusch

class teaMug:
    """Represents amount of tea in a mug"""

mug = teaMug()

mug.color = "yellow"
mug.size = "14 ounces"
mug.shape = "cube"
mug.amount = 14

import math

def tea_drinking_simulation(t, minutes):
    remaining_amount = t.amount - 2*minutes    #When 2 ounces are drank every minute 
    result = "My %s %s %s mug has"%(t.size, t.color, t.shape), remaining_amount, "ounces left after", minutes, "minutes"
    print(result)

tea_drinking_simulation(mug, 4)

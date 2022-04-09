import random
from pprint import pprint
SUNKEN_SHIP_PICS = [
    # The capital letters indicate that this is
    # not to be changed, under any circumstances.
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
     t
""",
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
""", 
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~~         ~~~~~~
""", 
"""
      /|\
     /_|_\
   ____|____
~~~         ~~~~~~
""", 
"""
      /|\
     /_|_\
~~~~~     ~~~~~~~~
""", 
"""
      /|\ 
~~~~~~   ~~~~~~~~~
""", """
~~~~~~~~~~~~~~~~~~
"""]

words = 'clam crab manatee turtle cuttlefish prawn \
        sponge shrimp squid lobster mackerel seal hammerhead \
        sealion marlin pufferfish octopus dolphin sunfish seahorse \
        stringray eagleray whaleshark clownfish starfish toadfish'.split()
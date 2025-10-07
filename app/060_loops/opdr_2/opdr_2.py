# Opdracht 2 loops
# Naam student: Jesper Pot
# Groep:ITFLEX

# Hier komt je code...

# Hier start de for-loop

import random

cijfers = []

for i in range(10, 101, 10):
    cijfers.append(i)

random.shuffle(cijfers)

print(cijfers)

exit()

import random
nl = [int(input()),]
for i in range(9):
	nl.append( random.randint(1, 100))
i = random.randint(0,9)
nl[i],nl[0] = nl[0],nl[i]
print(nl)

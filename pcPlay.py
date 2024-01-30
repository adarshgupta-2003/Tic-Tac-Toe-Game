from random import randint

def pc_play(list_1):
	while(1):
		number = randint(1,9)
		#number = think.think(list_1)
		if(list_1[number-1]=="X" or list_1[number-1]=="O"):
			continue
		else:
			break
	return number
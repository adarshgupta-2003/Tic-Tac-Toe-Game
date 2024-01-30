import signChoose
import pattern
import numberChoice
import check
import pcPlay


def play_with_pc(list_1):
	name = input("Name : ")
	sign=signChoose.sign_choose(name)
	if(sign=="O"):
		pc_sign = "X"
	else:
		pc_sign = "O"
	i=1
	while(i<=5):
		pattern.pattern(list_1)
		number_1 = numberChoice.number_choice(list_1)
		list_1[number_1-1]=sign
		check_variable=check.check(list_1)
		if(check_variable==True):
			break
		if(i<=4):
			number_2=pcPlay.pc_play(list_1)
			list_1[number_2-1]=pc_sign
		check_variable=check.check(list_1)
		if(check_variable==True):
			name = "PC"
			break
		i+=1
	pattern.pattern(list_1)
	if(i==6):
		print("Draw. ")
	else:
		print(f"{name} won. ")
	input()
import signChoose
import pattern
import numberChoice
import check


def play_with_player(list_1):
	player_1_name = input("Player 1 Name : ")
	player_2_name = input("Player 2 Name : ")
	player_1_sign = signChoose.sign_choose(player_1_name)
	if(player_1_sign=="O"):
		player_2_sign = "X"
	else:
		player_2_sign = "O"
	print(f"{player_1_name}, your sign is {player_1_sign}.")
	print(f"{player_2_name}, your sign is {player_2_sign}.")
	i=1
	while(i<=9):
		pattern.pattern(list_1)
		number_1 = numberChoice.number_choice(list_1)
		if(i%2!=0):
			list_1[number_1-1]=player_1_sign
		else:
			list_1[number_1-1]=player_2_sign
		check_variable = check.check(list_1)
		if(check_variable==True):
			break
		i+=1
	pattern.pattern(list_1)
	if(i==10):
		print("The match is draw.")
	else:
		if(i%2!=0):
			print(f"{player_1_name} won.")
		else:
			print(f"{player_2_name} won.")
	input()
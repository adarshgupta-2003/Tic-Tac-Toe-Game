def number_choice(list_1):
	while(1):
		number = (input("Enter the number you want to put your sign. "))
		if(number == "1" or number == "2" or number == "3" or number == "4" or number == "5" or number == "6" or number == "7" or number == "8" or number == "9"):
			number = int(number)
			if(list_1[number-1]=="X" or list_1[number-1]=="O"):
				print("The position is already taken. ")
			else:
				break
		else:
			print("Invalid Choice")
	return number
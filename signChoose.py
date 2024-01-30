def sign_choose(name):
	print(f"Welcome, {name}")
	print("Choose a sign :- either X or O")
	while(1):
		sign = input("Sign : ").upper()
		if(sign=="X"):
			break
		elif(sign=="O"):
			break
		else:
			print("Invalid Choice")
	return sign
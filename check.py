def check(list_1):
	if(list_1[0]==list_1[1]==list_1[2]):
		return True
	else:
		if(list_1[0]==list_1[3]==list_1[6]):
			return True
		else:
			if(list_1[0]==list_1[4]==list_1[8]):
				return True
			else:
				if(list_1[1]==list_1[4]==list_1[7]):
					return True
				else:
					if(list_1[2]==list_1[5]==list_1[8]):
						return True
					else:
						if(list_1[2]==list_1[4]==list_1[6]):
							return True
						else:
							if(list_1[3]==list_1[4]==list_1[5]):
								return True
							else:
								if(list_1[6]==list_1[7]==list_1[8]):
									return True
								else:
									return False
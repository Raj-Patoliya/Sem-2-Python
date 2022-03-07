def match(string):
	temp = 0
	for x in string:
		if x == "(":
			temp = temp + 1		
		elif x == ")":
			if(temp > 0):
				temp = temp -1
			else :
				return False
	if temp == 0:
		return True
	else :
		return False
string = input("\n\tEnter String : ")
print(match(string))

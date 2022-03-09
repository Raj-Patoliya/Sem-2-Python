size = int(input("\n\tEnter Numbers of element : "))
numlist = list(map(int,input("\nEnter the numbers : ").strip().split(",")))[:size]
temp = 0
for i in numlist:
	flag = 1
	for x in range(2,i):
		if i % x >= 1:					
			flag = 1
		else:
			flag = 0
			break
	if flag == 1:
	 	temp += i
print(numlist)
print(temp)

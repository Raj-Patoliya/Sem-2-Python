numlist = [1,2,3,4,5,0,1,2,0]
val = int(input("\n\tEnter Vlaue of Sum"))
print(numlist)

for i in range(len(numlist)) :
	for x in range((i+1),len(numlist)) :
		if numlist[i] + numlist[x] == val :
			print(numlist[i],numlist[x])

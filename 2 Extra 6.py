def index(numlist,num) :
	for x in range(0,num) :
		numlist.append(numlist[0])
		numlist.remove(numlist[0])
	return numlist
numlist = [1,2,3,4,5,6,7]
print(numlist)
num =  int(input("\n\tEnter Value  : "))
print(index(numlist,num))

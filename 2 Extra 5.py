def index(numlist,num) :
	a=0
	for x in numlist :
		if num == x :
			a
			break
		a = a+ 1
	return a
numlist = [10,2,5,3,7,8,8]
print(numlist)
num =  int(input("\n\tEnter Value  : "))
print("\n\t",num," is at index ",(index(numlist,num)))

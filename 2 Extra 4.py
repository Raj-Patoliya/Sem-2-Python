numlist = [10,2,5,3,7,8]
val1 =  int(input("\n\tEnter Value 1 : "))
val2 =  int(input("\n\tEnter Value 2 : "))
a=0
temp1 = 0
temp2 = 0
print(numlist)
for x in numlist :
	a = a+ 1
	if val1 == x :
		temp1 = a
	elif val2 == x : 
		temp2 = a
print("\n\tIndex difference ",val1,val2," is ",abs(temp1-temp2))

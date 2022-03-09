numlist = [1,2,0,1,2,0,1,2,0]
for x in numlist:
	if x ==  0:
		numlist.remove(x)
		numlist.append(0)
print(numlist)

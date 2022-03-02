def rev(num):
	thislist = []
	count = 0
	while(num >= 1):
		count= count + 1
		mod = num % 10
		thislist.append(mod)
		num = num / 10
	x = len(thislist)
	revnum = 0
	for xs in thislist :
		print(xs * (10^(x-1)) )
		print(revnum)
		revnum = revnum + xs * (10^(x-1))  
		
num = input("\n\t Enter The Number")

rev(num)

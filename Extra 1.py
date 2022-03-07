def rev(num):
	thislist = []
	revnum = 0
	while(num >= 1):
		mod = num % 10
		revnum = int(revnum * 10 + mod) 	
		num = num / 10
	return(revnum)		

num = input("\n\tEnter The Number")
x = rev(int(num))
print("\n\tReversed Value  =  ",x)
print("\n\tType of Reversed Value = ",type(x))

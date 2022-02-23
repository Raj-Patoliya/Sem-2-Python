# Write  a  program  which  will  allow  user  to  enter  10  numbers  and  display  largest  odd number  from  them.  It  will  display  appropriate  message  in  case  if  no  odd  number  is found

i=0
inplist = [0]*10
while(i != 10):
	inplist[i] = input("\n\tEnter The A["+str(i)+"]")
	i=i+1
temp = 0
count = 0
i = 0
while(i != 10):
	if int(inplist[i]) % 2 == 1 :
		count = count + 1
		if int(temp) < int(inplist[i]) :
			temp = inplist[i]
	i=i+1
if count == 0 :
	print("\n\t There is no odd Number")
else :
	print(str(temp))

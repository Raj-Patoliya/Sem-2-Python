# Write a Python program to check if the number provided by the user is an Armstrong number.

num = int(input("\n\tEnter the number : "))
temp = num
arm = 0
while(int(temp) > 0) :
	reminder = int(temp) % 10
	temp = temp / 10
	arm = arm + (reminder *reminder * reminder )
if num == arm :
	print("\n\t"+str(num)+" Number is Armstrong number")
else :
	print("\n\t"+str(num)+" Number is not Armstrong number")

#Write  a  program  in  python  to  find  out  maximum  and  minimum  number  out  of  three user entered number.

a = int(input("\n\tEnter First Number : "))
b = int(input("\n\tEnter Second Number : "))
c = int(input("\n\tEnter Third Number : "))

if a > b and a > c :
	print(a," is Biggest Number")

elif b > a and b > c :
	print(b," is Biggest Number")

elif c > b and c > a :
	print(c," is Biggest Number")

if a < b and a < c :
	print(a," is smallest Number ")

elif b < a and b < c :
	print(b," is smallest Number")

elif c < b and c < a :
	print(c," is smallest Number")

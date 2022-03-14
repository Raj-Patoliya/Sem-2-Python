lust = [ x for x in input().split(" ") ]
print(lust)
temp = 0
word = ""
for x in lust :	
	if len(x) > temp:
		temp = len(x)
		word = x
print(word,temp)

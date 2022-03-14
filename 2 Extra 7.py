def part(lust):
	eve =[]
	odd = []	
	list(filter(lambda x:eve.append(x) if  x%2 == 0 else odd.append(x),lust))
	print(eve)
	print(odd)
part(lust = [ int(x) for x in input().split(",") ])

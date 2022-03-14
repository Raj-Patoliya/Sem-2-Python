eve =[]
odd = []	
list(filter(lambda x:eve.append(x) if  x%2 == 0 else odd.append(x),(int(x) for x in input("\n\t").split(","))))
print("\n\t",eve,"\n\t",odd)

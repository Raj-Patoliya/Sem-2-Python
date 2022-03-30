def rainfallAvg(mylst):
  mydict = {}
  for i in mylst :
    if i[0] in mydict :
      mydict[i[0]].append(i[1])
    else :
      mydict[i[0]] = [i[1]]
  for i in mydict :
    avg = sum(mydict.get(i)) / len(mydict.get(i))
    mydict.update({i:avg})
  return mydict



mylst = []
size = input("Enter The Number of enteries : ")
for i in range(0,int(size)):
  temp = ()
  city = input("\n\tName of City : ")
  rainfall = input("\n\tRainfall of "+city+" : ")
  thistuple = (city,rainfall)
  temp = tuple(thistuple)
  mylst.append(temp)
print(rainfallAvg(mylst))

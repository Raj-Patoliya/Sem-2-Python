matchlist = {'test1':{'Kohli' : 500,'Pujara':102},'test2':{'Jadeja': 610,'Pujara':185,'Kohli':110}}
newdict = {}
for x in matchlist.values():
    for y in x :
      if y in newdict:
        newdict[y]=newdict[y]+x[y]
      else:
        newdict[y]=x[y]
print(max(newdict,key=newdict.get),"is orange cap winner with",max(newdict.values()))

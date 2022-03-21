lst = [1,2,3,4,5,6,7,8,9]
newlst = []
a = -1
for i in range(0,len(lst)) :
  a+=1
  if a>=len(lst)-1:
    newlst.append(lst[len(lst)-1] * lst[0])
  else :
    newlst.append(lst[a+1] * lst[a-1])
print(newlst)

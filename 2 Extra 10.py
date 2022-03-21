mylst = [ i for i in range(1,23)]
def myfun(newlist,n) :
  for i in range(0,len(newlist),n) : 
    yield newlist[i:i+n]
n = 5
chunk_list = list(myfun(mylst,5))
for x in chunk_list :
  print(x,end="\n")

newlst = []
def flatten(mylst) :
  for i in mylst :
    if type(i) == type([]) :
      flatten(i)
    else:
      newlst.append(i)
  return newlst
mylst = [ 1,2,[3,[10,20]],[4,[5,6]]]
print(flatten(mylst))

matrics = [[1,2,3,4],[4,5,6,7],[1,7,8,9]]
trans = [ [matrics[j][i] for j in range(0,len(matrics))] for i in range(0,len(matrics[0]))]
for i in matrics:
  print(i,end="\n")
print("\n\nTranspose:")
for i in trans:
  print(i,end="\n")

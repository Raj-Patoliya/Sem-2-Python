names = ['Ch','Dh','Eh','cb','Tb','Td',"Gc"]
mylst = list(filter(lambda x :True if "c" in x[0] else False ,names))
print(mylst)

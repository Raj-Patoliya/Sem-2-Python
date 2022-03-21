names = [x for x in range(1,100)]
mylst = list(filter(lambda x :(x*x) if (x*x) % 2 == 0 else False ,names))
print(mylst)

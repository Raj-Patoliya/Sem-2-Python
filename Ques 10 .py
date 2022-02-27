def fact(n):
    count = n
    if n==0:
        return
    num = 1
    while(count!=1):
        num = num * count
        count= count - 1
    print(num)    
    n= n-1
    fact(n)
n = int(input("\n\tEnter Number : "))
fact(n)

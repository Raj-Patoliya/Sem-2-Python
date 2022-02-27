def fibo(n,n1,n2):
    if n == 0 :
        return
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    n = n - 1
    print(" "+str(n3))
    fibo(n,n1,n2)
    
n = int(input("\n\tEnter Number : "))
print(" 0")
print(" 1")
fibo(n,0,1)



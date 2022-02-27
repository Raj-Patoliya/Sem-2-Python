

string = input("\n\tEnter String  : ")
i = 0
count = 0 
for s in string :
    i = i + 1
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' :  
        count = count + 1 
print("\n\tThere are "+str(count)+" vovels in given string")
print("\n\tLength of given string is "+str(i))
print("\n\tReverse of given string is "+string[::-1])
if string == string[::-1] :
    print("\n\tGiven String is Palindrom string")
else :
        print("\n\tGiven String is not Palindrom string")
old = input("\n\tEnter Word to be replaced  : ")
new = input("\n\tEnter new word  : ")
x = string.replace(old,new)
print("\n\tUpdated string : "+x)


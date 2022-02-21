# Write a program in python to swap two variables without using temporary variable

a = input("\n\t Enter The Value For First Element : ")

b = input("\n\t Enter The Value For Second Element : ")

print("\n\t Value Before Swap")
print("\n\tA :"+str(a))
print("\n\tB :"+str(b))
a ^= b 
b ^= a 		
a ^= b 
print("\n\t Value After Swap")
print("\n\tA :"+str(a))
print("\n\tB :"+str(b))

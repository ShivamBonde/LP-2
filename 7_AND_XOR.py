string="hello world"
a=len(string)

print("and: ")
for i in range(a):
    ans1=ord(string[i]) & 127
    print(ans1,end=" ")
    
print("\nxor: ")
for i in range(a):
    ans2=ord(string[i]) ^ 127
    print(ans2,end=" ")
    
    
    

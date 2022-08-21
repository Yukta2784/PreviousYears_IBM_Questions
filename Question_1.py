#WAP to find HCF of two space seperated numbers.
import re
n=input()
l1=[]
l2=[]
j=re.split(r" ",n)

for i in range(1,(int(j[0])+1)):
    if(int(j[0])%i==0 and int(j[1])%i==0):
    
        l1.append(i)
    
print(max(l1))

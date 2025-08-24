a=input("Enter the number to check narcissistic: ")
n=len(a)
d=0
for i in a:
    d+=int(i)**n
if d==int(a):
    print("is narcissistic")
else:
    print("nono")

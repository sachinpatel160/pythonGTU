a=int(input("Enter a value of a: "))
b=int(input("Enter a value of b: "))
c=int(input("Enter a value of c: "))

'''if a>b:                 #if for checking condition a>b
    if a>c:             #nested if for checking condition a>c
        print ("A is greater")
    else:
        print ("C is greater")
else:
    if b>c:             #nested if for checking condition b>c
        print ("B is greater")
    else:
        print ("C is greater")
'''
'''if a>b and a>c:
    print ("A is greater")
elif b>a and b>c:
    print ("B is greater")
else:
    print ("C is greater")
'''
print (max(a,b,c))

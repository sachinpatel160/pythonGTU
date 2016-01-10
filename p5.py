x=int(input("Enter a value of first value : "))     #first value
y=int(input("Enter a value of aSecond value: "))        #second value

print("1. For addition")
print ("2. For substraction")
print ("3. For multiplication")
print ("4. For division")
print ("5. For module")
a=int(input("Press your selection : "))     #ask for action

if a==1:
      print (x+y)       #addition
elif a==2:
      print (x-y)       #substraction
elif a==3:
      print (x*y)       #multiplication
elif a==4:
      print (x/y)       #division
elif a==5:
      print (x%y)       #modulo
else:
      print ("Enter a proper value...")     #else part

#we can use format() function for formatting the output.

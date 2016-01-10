for i in range(0,10):       #loop to define numbers
    if i>5:
        for j in range(4,0,-1):
            print (j*"*")
        break
    else:
        print (i*"*" )    #i is a variable to iterate

'''
Output:
*
**
***
****
*****
****
***
**
*
'''

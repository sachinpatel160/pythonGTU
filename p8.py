fopn=open("file.txt","r")       #open file
for line in fopn:       $               #read line by line
    if "sachin" in line:
        print (line)
fopn.close()

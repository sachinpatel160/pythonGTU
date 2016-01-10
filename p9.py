
try:
    sp=open("edit.txt","w")
    sp.write("I am sachin patel\n")
    sp.write("I am sachin\n")
    sp.write("I am\n")
    sp.write("I\n")
    sp.write("I am sachin patel\n")
    sp.close()

    sp=open("edit.txt","r")
    spr=sp.read()
    print(spr)
    sp.close()

    sp=open("edit.txt","w")
    ghr=["Dear it is called typing\n","je tu nathi karto"]
    sp.writelines(ghr)
    sp.close()

    sp=open("edit.txt","r")
    spr=sp.read()
    print(spr)
    sp.close()

except:
    print ("An error occured while writing file:")
sp.close()

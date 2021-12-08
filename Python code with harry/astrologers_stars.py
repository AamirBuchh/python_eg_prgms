"""
To give a certain input as a number which then prints out that no of lines of certain pattern of asterisks(*) on specified number of lines. We have two patterns on for a string entered and other for empty string as(for number = 3):
--pattern 1(for string)--

*
**
***

--pattern 2(for no string)--

***
**
*
---
""" 
y_n = "Y"   # intialiazation
while(y_n == "Y" or y_n == "y"): #loop for repeating the program
    int_n = input("Enter the number of rows of star pattern : ")    #no of lines entered here
    if int_n.isnumeric():
        intr = int(int_n)
        typ_ip = input("Enter some string or press enter : ")       #enter string or no string here
        if bool(typ_ip) == True:    #for string
            for i in range(1,intr+1):
                print("*"*i,end="")
                print("")
        elif bool(typ_ip) == False:     #for no string
            for j in range(intr,0,-1):
                print("*"*j,end="")
                print("")
        y_n = input("Continue(Y/N)?")
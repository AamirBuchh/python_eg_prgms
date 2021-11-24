# print list using given index

"""def list_print(index):
    print(list1[index])
    
    
list1=["Aamir","Hamid","Jamil"]
index=int(input("Index to access : "))
list_print(index)"""

# which of 2 nos is greatest

"""def grt_of_2(num1,num2):
    if(num1>num2):
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")


grt_of_2(2,3)
grt_of_2(5,3)
grt_of_2(21,8)
grt_of_2(21,30)
grt_of_2(12,13)"""

# which is greatest of 3 nos

"""def grt_of_3(num1,num2,num3):
    if(num3>num1)and (num3>num2):
        print(f"{num3} is greatest of 3 nos")
    else:
        if(num1>num2):
            print(f"{num1} is greatest of 3 nos")
        else:
            print(f"{num2} is greatest of 3 nos")

grt_of_3(1,2,3)
grt_of_3(12,20,18)"""

# greatest of 4 nos

"""def grt_of_4(num1,num2,num3,num4):
    if (num4>num1)and (num4>num2) and (num4>num3):
        print(f"{num4} is greatest")
    else:
        if (num3>num1)and (num3>num2) and (num3>num4):
            print(f"{num3} is greatest")
        else:
            if (num2>num1)and (num2>num3) and (num2>num4):
                print(f"{num2} is greatest")
            else:
                print(f"{num1} is greatest")

grt_of_4(1,2,3,4)"""

# try except

"""a=10
b=0
names=["Aamir","Jamil","Hamid"]
try:
    result=a/b
    print(names[6])
except IndexError:
    print("Index error")
except ZeroDivisionError:
    print("The number cannot be divided by zero")"""

# different functions


"""names=["Aamir","Jamil","Hamid"]
length=len(names)
print(f"length of names list is : {length}")
nos=[11,30,100,12,15]
minimum=min(nos)
print(f"min of nos is : {minimum}")
print(max(nos))"""

"""a="Hello World"
print(a.upper())
print(a.lower())
nos=[11,30,100,12,15]
print(sorted(nos))
print(sum(nos))"""

"""nos=[11,30,100,12,15]
nos.append(1)
nos.remove(11)
print(nos)"""

# Form Details

"""def get_age()

print("Enter details for your form")
name=input("Enter your name : ")
age=input("Enter your age : ")
p_no=input("Enter your phone no : ")
addr=input("Enter your address : ")
e_mail=input("Enter your email : ")

print()
print(f"Check your details : ")
print()
print(f"NAME : {name} \nAGE : {age} \nPHONE NO : {p_no} \nADDRESS : {addr} \nE.MAIL : {e_mail}")"""

# Raise

"""def printint(value):
    if type(value)==str:
        raise Exception("Value must be number")
    elif value>10:
        raise ValueError("Value must be less than zero")
    else:
        print("Value is less than 10")"""

# Append



"""print("Enter details for your form")
name=input("Enter your name : ")
assert type(name)==str,"Name has to be string"
age=input("Enter your age : ")
assert int(age) > 0,"Age has to be greater than zero"
p_no=input("Enter your phone no : ")
assert type(p_no)==int,"P.no has to be integer"
addr=input("Enter your address : ")
assert type(addr)==str,"Address has to be string"
e_mail=input("Enter your email : ")
assert type(e_mail)==str,"Email has to be string"
print()
print(f"Check your details : ")
print()
print(f"NAME : {name} \nAGE : {age} \nPHONE NO : {p_no} \nADDRESS : {addr} \nE.MAIL : {e_mail}")"""

"""file_even=open('C:/Users/HP-PC/Desktop/even.txt',mode='w')
file_odd=open('C:/Users/HP-PC/Desktop/odd.txt',mode='w')

def even_odd_sorter(num_in):
    for num in range(1,num_in):

        if num%2 == 0:
            print(f"{num} is even\n")
            file_even.write(str(num)+" is even \n")
            

        else :
            print(f"{num} is odd\n")
            file_odd.write(str(num)+" is odd \n")
            
       

even_odd_sorter(int(input("Enter the range of number : ")))
file_even.close()
file_odd.close()"""

# greatest of five

"""def grt_of_five(num1,num2,num3,num4,num5):
    if(num1>num2)and(num1>num3)and(num1>num4)and(num1>num5):
        print(f"{num1} is greater than {num2},{num3},{num4} and {num5} ")
    elif(num2>num1)and(num2>num3)and(num2>num4)and(num2>num5):
        print(f"{num2} is greater than {num1},{num3},{num4} and {num5} ")
    elif(num3>num1)and(num3>num2)and(num3>num4)and(num3>num5):
        print(f"{num3} is greater than {num1},{num2},{num4} and {num5} ")
    elif(num4>num1)and(num4>num2)and(num4>num3)and(num4>num5):
        print(f"{num4} is greater than {num1},{num2},{num3} and {num5} ")
    else:
        print(f"{num5} is greater than {num1},{num2},{num3} and {num4} ")


num1=int(input("Enter the 1st no: "))
num2=int(input("Enter the 2nd no: "))
num3=int(input("Enter the 3rd no: "))
num4=int(input("Enter the 4th no: "))
num5=int(input("Enter the 5th no: "))

grt_of_five(num1,num2,num3,num4,num5)"""

# add using return to variable

"""def add_two_nos(a,b):
    c=a+b;
    return(c);

d=add_two_nos(int(input("Enter the first no : ")),int(input("Enter the second no : ")))
print(d)"""

# count vowels and consonents in a given string

def vow_conso_con(string):
    vowel_con = 0
    cons_con = 0
    str_len = len(string)
    len_con = 0
    loop_con = 0
    for i in string:
        loop_con += 1
        #to include both upper and lower case vowels
        if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u") or (i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U"):
            vowel_con += 1
            if loop_con <= str_len:
                continue
            else:
                break

        elif i == " ":        #to exclude spaces
            continue

        elif type(i) == int:  #to exclude numbers
            continue

        elif type(i) == str:  #for consonent case
            cons_con += 1;
            if loop_con <= str_len:
                continue
            else:
                break
        else:                 #for symbols other than string
            continue
    return(vowel_con,cons_con)

no_vowel,no_conso = vow_conso_con(input("Enter the string : "))
print(f"vowels = {no_vowel} and consonents = {no_conso}")











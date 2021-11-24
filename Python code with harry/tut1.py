# print(" Hello World",end=" ")
# print("!")
#created a dictionary for a user who is entering the input string
# dict1 = {"append":"add","del":"delete","update":"this function updates dictionary","upper":"upper case","lower":"lower case"}
# print(dict1[input("Enter the word : ")])
#Looping
list1 = [["harry",1],["aamir",2],["hamid",3]]
dict1 = dict(list1)
# print(dict1)
# for name,item in list1:
#     print(name,":",item,end=" ")
# for name,item in dict1.items():
#     print(name,":",item,end=" ")
for thing in dict1.items():         #.items accesses the value and the key of a dictionary
    print(thing)
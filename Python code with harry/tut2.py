# items = [int,float,"Hello",1,2,4,21,23,453,32,123]
# for item in items:
#     if type(item) == int:
#         if item>6:
#             print(item)

# while loop

# i=0
# while(i<25):
#     print(i,end=' ')


# break and continue

# i=0
# while(i<100):
#     i = i+1
#     if i==18 or i ==13 or i ==1:
#         continue
#     print(i,end=' ')
#     if i==25:
#         break
# # break gets the loop here

# i=0
# while(i<=100):
#     i = int(input())
# print("\n\n***Congrats! Entered no greater than 100***\n\n")

while(True):
    inp = int(input("Enter a number :"))
    if inp>100:
        print("You entered no greater than 100\n")
        break
    else:
        print("Try Again\n")
        continue

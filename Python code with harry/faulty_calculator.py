# Faulty calculator
# 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4

first_no = input("First No : ")
op = input("Operation : ")
second_no = input("Second No : ")
flag = first_no +" "+op+" "+ second_no
if flag == "45 * 3":
    print("45 * 3 = 555")
elif flag == "56 + 9":
    print("56 + 9 = 77")
elif flag == "56 / 6":
    print("56 / 6 = 4")
elif op in ["+","-","*","/"]:
    if op == "+":
        print(f"{first_no} + {second_no} = {int(first_no)+int(second_no)}")
    if op == "-":
        print(f"{first_no} - {second_no} = {int(first_no)-int(second_no)}")
    if op == "*":
        print(f"{first_no} * {second_no} = {int(first_no)*int(second_no)}")
    if op == "/":
        print(f"{first_no} / {second_no} = {int(first_no)/int(second_no)}")
else:
    print("Not valid inputs or operators")
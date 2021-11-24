# code find the direction North(N),South(S),West(W) and East(E)
# with intial direction as North(N) signified by variable in_dir
# we provide direcion from as Left->L and Right->R from variable
# ins_g to go left or right
# eg(with north as initial direction)
# input --> LLR   (in UPPER case only)
# output --> W     (i.e. west)
print("code find the direction North(N),South(S),West(W) and East(E) with intial direction\n as North(N) signified by variable in_dir we provide direcion from as Left->L\n and Right->R from variable ins_g to go left or right eg(with north as initial direction)\n input --> LLR   (in UPPER case only) output --> W     (i.e. west)\n")
ins_g = input("Enter the code : ")
in_dir = "N"
lst_ins = list(ins_g)
lst_ins.append(0)
for ins in lst_ins:


    if ins == "R" and in_dir == "N":
        in_dir = "E";
    elif ins == "L" and in_dir == "N":
        in_dir = "W";


    elif ins == "R" and in_dir == "S":
        in_dir = "W";
    elif ins == "L" and in_dir == "S":
        in_dir = "E";


    elif ins == "R" and in_dir == "W":
        in_dir = "N";
    elif ins == "L" and in_dir == "W":
        in_dir = "S";


    elif ins == "R" and in_dir == "E":
        in_dir = "S";
    elif ins == "L" and in_dir == "E":
        in_dir = "N";
    elif ins == 0:
        print(in_dir);
        break;
    else:
        print("Not a valid input!!");
        break;
        

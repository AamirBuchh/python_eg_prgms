for num in range(1,100):
    if(num==1):
        print(num)
    elif(num==2):
        print(num)
    else:
        for divisor in range(2,100):
            if (num%divisor)==0:
                break
            else:
                divisor+=1
                if divisor<num:
                    continue
                else:
                    print(num)
                    break

s=51000

if(s>=100000):
    t=s+(s*0.05)
    print("salary is")
    print(t)
    
elif(s>=50000 and s<100000):
    t=s+(s*0.1)
    print("salary is")
    print(t)
    
elif(s>=25000 and s<50000):
    t=s+(s*0.15)
    print("salary is")
    print(t)
    
elif(s>=10000 and s<25000):
    t=s+(s*0.18)
    print("salary is")
    print(t)
    
else:
    print("not valid input")
    

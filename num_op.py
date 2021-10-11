def primedetect(num):
    if num == 1:
        print(num)
    elif num == 2:
        print(num)
    else:
        for divisor in range(2, 100):
            if (num % divisor) == 0:
                break
            else:
                divisor += 1
                if divisor < num:
                    continue
                else:
                    print(num)
                    break


def sign(num):
    if num >= 0:
        print("no is positive")
    else:
        print("no is negative")

def swap(a, b):
    print("a=", a)
    print("b=", b)
    a = a + b
    b = a - b
    a = a - b
    print("a=", a)
    print("b=", b)


def grt_of_2(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")


def grt_of_3(a, b, c):
    if (c > a) and (c > b):
        print("c is greatest of 3 nos")
    else:
        if a > b:
            print("a is greatest of 3 nos")
        else:
            print("b is greatest of 3 nos")


grt_of_3(21, 10, 1)

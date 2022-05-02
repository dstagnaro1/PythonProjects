import sys

def sqrt(x):
    z = 1.0
    roots = [1,1,1]
    while True:
        z -= (z*z - x) / (2*z)
        if z in roots:
            break
        else:
            roots.pop()
        roots.insert(0,z)
        
    return z

entered_num = False

if len(sys.argv) > 1:
    if sys.argv[1] != "0":
        try:
            num = sys.argv[1]
            num = int(num)
        except ValueError:
            print("Entered a non number")
            exit()
else:
    while not entered_num:
        try:
            num = input("Enter number to get square root ")
            num = int(num)
            entered_num = True
        except ValueError:
            print("Entered a non number")
    

print(sqrt(num))

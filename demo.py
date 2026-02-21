x=30
y=15
z=26
if x>y:
    if x>z:
        print("x is greatest")
        if y>z:
            print("y is second greatest")
            print("z is least")
        else:
            print("z is second greatest")
            print("y is least")
    else:  
        print("x is second  greatest")
        print("z is greatest    ")
        print("y is least")
else:
    if y>z:
        print("y is greatest")
        if x>z:
            print("x is second greatest")
            print("z is least")
        else:
            print("z is second greatest")
            print("x is least")
    else:
        print("y is second greatest")
        print("z is greatest")
        print("x is least")
    
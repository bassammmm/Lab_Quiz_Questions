
def image(l,b):
    for x in range(0,l):
        print("\n")
        for y in range(0,b):
            if x==0 or x==(l-1):
                print("*",end="  ")

            else:
                if y==0 or y==(b-1):
                    print("*",end="  ")
                else:
                    if y==1 or y==(b-2):
                        print("+",end="  ")
                    elif x==1:
                        print("+",end="  ")
                    elif x==(l-2):
                        print("+",end="  ")        
                    else:
                        print(" ",end="  ")
                    
length  = int(input("Please enter the length of the box  : "))
breadth = int(input("Please enter the breadth of the box : "))
image(length,breadth)

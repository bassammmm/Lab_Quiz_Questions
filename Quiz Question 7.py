def ones_compliment(num):
    c = "{0:b}".format(num)
    clst = list(c)
    if len(clst)<4:
        while len(clst)<4:
            clst.insert(0,'0')
    for change in range(0,4):
        if clst[change]=='0' or clst[change]==0 :
            clst[change]='1'
        else:
            clst[change]='0'
    num2 = clst
    num3 = num2[0]+num2[1]+num2[2]+num2[3]
    binary = '0b'
    decimal_str = binary+num3
    decimal = int(decimal_str,2)
    print("\n1's Compliment of ",num,"is :",num3,"which in decimal form is :",decimal)
    
def twos_compliment(num):
    c = "{0:b}".format(num)
    clst = list(c)
    if len(clst)<4:
        while len(clst)<4:
            clst.insert(0,'0')
    for change in range(0,4):
        if clst[change]=='0' or clst[change]==0 :
            clst[change]='1'
        else:
            clst[change]='0'
    num2 = clst
    num3 = num2[0]+num2[1]+num2[2]+num2[3]
    binary = '0b'
    decimal_str = binary+num3
    decimal = int(decimal_str,2)
    decimal += 1
    binary = "{0:b}".format(decimal)
    blst = list(binary)
    while len(blst)<4:
            blst.insert(0,'0')
    num4 = blst[0]+blst[1]+blst[2]+blst[3]
            
    print("\n2's Compliment of ",num,"is :",num4,"which in decimal form is :",decimal)
    

    
    
user_num = int(input("Please enter a number between 0-15: "))
while user_num<0 or user_num>15:
    print("Please enter a number only between 0-15!")
    user_num = int(input("Please enter a number between 0-15: "))
if user_num>=0 and user_num<=15:
    ones_compliment(user_num)
    twos_compliment(user_num)

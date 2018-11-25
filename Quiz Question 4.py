
coffee = int(input("How many cups of coffee        : "))
coffee_fee = 25*coffee
money = int(input("How much money did you recieve : "))
change_to_be_given = money-coffee_fee
print("Coffee Fee              :",coffee_fee)
print("Money to be Returned    :",change_to_be_given)

user = str(change_to_be_given)
user_int = int(user)
user_lst = list(user)
b = []
for x in range(len(user_lst)):
    a = int(user_int%10)
    user_int = user_int/10
    b.append(a)
b.reverse()


_1000 = 0
_500  = 0
_100  = 0
_50   = 0
_20   = 0
_10   = 0
_5    = 0
_1    = 0


if len(b)==4:
    _1000 += b[0]
    if b[1]>=5:
        _500 += 1
        c = b[1]-5
        _100 += c
    else:
        _100 += b[1]
    if b[2]>=5:
        _50 += 1
        d = b[2]-5
        if d>=2 and d<4:
            _20 += 1
            e = d-2
            _10 += e
        elif d>=4:
            _20 +=2
            f = d-4
            _10 +=f
        else:
            _10 += d
    else:
        if b[2]>=2 and b[2]<4:
            _20+=1
            h=b[2]-2
            _10+=h
        elif b[2]>=4:
            _20+=2
            i=b[2]-4
            _10+=i
        else:
            _10+=b[2]
    if b[3]>=5:
        _5 +=1
        g=b[3]-5
        _1 += g
    else:
        _1 +=b[3]
        
elif len(b)==3:
    if b[0]>=5:
        _500 += 1
        c = b[0]-5
        _100 += c
    else:
        _100 += b[0]
    if b[1]>=5:
        _50 += 1
        d = b[1]-5
        if d>=2 and d<4:
            _20 += 1
            e = d-2
            _10 += e
        elif d>=4:
            _20 +=2
            f = d-4
            _10 +=f
        else:
            _10 += d
    else:
        if b[1]>=2 and b[1]<4:
            _20+=1
            h=b[1]-2
            _10+=h
        elif b[1]>=4:
            _20+=2
            i=b[1]-4
            _10+=i
        else:
            _10+=b[1]
    if b[2]>=5:
        _5 +=1
        g=b[2]-5
        _1 += g
    else:
        _1 +=b[2]

if len(b)==2:
    if b[0]>=5:
        _50 += 1
        d = b[0]-5
        if d>=2 and d<4:
            _20 += 1
            e = d-2
            _10 += e
        elif d>=4:
            _20 +=2
            f = d-4
            _10 +=f
        else:
            _10 += d
    else:
        if b[0]>=2 and b[0]<4:
            _20+=1
            h=b[0]-2
            _10+=h
        elif b[0]>=4:
            _20+=2
            i=b[0]-4
            _10+=i
        else:
            _10+=b[0]
    if b[1]>=5:
        _5 +=1
        g=b[1]-5
        _1 += g
    else:
        _1 +=b[1]

        
print("1000 * ",_1000)
print("500  * ",_500)
print("100  * ",_100)
print("50   * ",_50)
print("20   * ",_20)
print("10   * ",_10)
print("5    * ",_5)
print("1    * ",_1)

        
        

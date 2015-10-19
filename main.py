originArray = [[1,2,3],[4,5,6],[7,8,9]]
finalArray = []

# append to final array leftmost column of origin array
def goUp(a):
    for i in range(0, len(a)):
        finalArray.append(a[len(a)-1-i].pop(0))
    return a

# append to final array last row of origin array
def goLeft(a):
    for i in range(0, len(a[-1])):
        finalArray.append(a[-1].pop())
    return del_items(a, ':-1')

# append to final array rightmost column of origin array
def goDown(a):
    for i in range(0, len(a)):
        finalArray.append(a[i].pop())
    return a

# append to final array first row of origin array
def goRight(a):
    for i in range(0, len(a[0])):
        finalArray.append(a[0][i])
    return del_items(a, '1:')

# remove first or last row
def del_items(a, delStr):
    if delStr.startswith('1'):
        return a[1:]
    else:
        return a[:-1]


while originArray:
    originArray = goRight(originArray)
    if not originArray:
        break
    else:
        originArray = goDown(originArray)
        if not originArray:
            break
        else:
            originArray = goLeft(originArray)
            if not originArray:
                break
            else:
                originArray = goUp(originArray)

print finalArray

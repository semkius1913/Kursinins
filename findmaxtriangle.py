
import random
import math

def binaryToDecimal(x):
    value = 0
    t = x.copy()
    for i in range(len(t)):
        digit = t.pop()
        if digit == 1:
            value = value + pow(2, i)
    return value


def roulettewheel(choices):
    maxi = sum(choices)
    decide = random.uniform(0, maxi)
    current = 0
    number = 0
    for choice in choices:
        current += choice
        if current > decide:
            return number
        number += 1


def sign(x1, y1, x2, y2, x3, y3):
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)

def PointInTriangle(x0, y0, x1, y1, x2, y2, x3, y3):

    d1 = sign(x0, y0, x1, y1, x2, y2)
    d2 = sign(x0, y0, x2, y2, x3, y3)
    d3 = sign(x0, y0, x3, y3, x1, y1,)

    has_neg = bool(d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = bool(d1 > 0) or (d2 > 0) or (d3 > 0)
    if ((has_neg and has_pos) == True):
        return False
    else:
        return True


def createrandomnumber(x):
    tempr = []
    for j in range(x):
        temp2 = random.randint(0, 1)
        tempr.append(temp2)
    return tempr


filename = "inout/pic0.txt"
lines2 = []
f = open(filename, "r")
allofit = f.read()
lines = allofit.split("\n")


for st in lines:
    liist = st.split(", ")
    lines2.append(liist)


lines = lines2.copy()
#  print(lines)
f.close()

#106 66
#90 91
#122 93
#78 88   104 83
#print(PointInTriangle(104, 83, 106, 66, 90, 91, 122, 93))


#  Get number of individuals and number of features with a default of 4 and 5
try:
    indNum = int(input("Enter number of individuals: "))
except ValueError as err:
    print("error:")
    print(err)
    print("setting individuals number to default")
    indNum = 960
try:
    featNum = int(input("Enter number of features: "))
except ValueError as err:
    print("error:")
    print(err)
    print("setting features number to default")
    featNum = 8

divider = indNum / 6 + 1

print("Number of individuals:", indNum, "Number of features:", featNum)

#  generate sequences of 0 and 1 for individuals
individualsInBinary = []
for i in range(indNum):
    individualsInBinary.append(createrandomnumber(featNum))
#  print(individualsInBinary)

individualsInDecimal = []

for x in individualsInBinary:
    val = binaryToDecimal(x)
    individualsInDecimal.append(val)

#print(individualsInDecimal)

binoms = []
bbinoms = []
trinoms = []
btrinoms = []
fulls = []
bfulls = []

flg1 = 0
flg2 = 0



for i in range(len(individualsInDecimal)-1):
    if (i % 2 == 0):
        y = individualsInDecimal[i]
        x = individualsInDecimal[i+1]
        by = individualsInBinary[i]
        bx = individualsInBinary[i + 1]
        while (int(lines[y][x]) == 0):
            individualsInBinary[i] = createrandomnumber(featNum)
            individualsInBinary[i+1] = createrandomnumber(featNum)
            individualsInDecimal[i] = binaryToDecimal(individualsInBinary[i])
            individualsInDecimal[i+1] = binaryToDecimal(individualsInBinary[i+1])
            y = individualsInDecimal[i]
            x = individualsInDecimal[i + 1]
            by = individualsInBinary[i]
            bx = individualsInBinary[i + 1]

        binoms.append(y)
        bbinoms.append(by)
        binoms.append(x)
        bbinoms.append(bx)
        if flg1 == 0:
            flg1 = 1
            trinoms.append(binoms)
            btrinoms.append(bbinoms)
        elif flg2 == 0:
            flg2 = 1
            trinoms.append(binoms)
            btrinoms.append(bbinoms)
        else:
            trinoms.append(binoms)
            btrinoms.append(bbinoms)
            fulls.append(trinoms)
            bfulls.append(btrinoms)
            trinoms = []
            btrinoms = []
            flg1 = 0
            flg2 = 0
        binoms = []
        bbinoms = []

#  now fulls[] are my individuals where features are 3 pixels with y,x coordinates
#  ( fulls-> [individual(coordinates)]-> [yx])
#  print('fulls')
#  print(fulls)
#print(bfulls)
statement = 0
maxim = []
maxim.append(0)
print('dots, [[1y 1x], [2y, 2x], [3y, 3x]], iteration')
while statement < 3000:




    sqares = []
    pairs = []
    fields = []



    for i in fulls:
        pairs.append(min(i[0][0], i[1][0], i[2][0]))
        pairs.append(min(i[0][1], i[1][1], i[2][1]))
        pairs.append(max(i[0][0], i[1][0], i[2][0]))
        pairs.append(max(i[0][1], i[1][1], i[2][1]))
        sizeoffield= (pairs[2] - pairs[0]) * (pairs[3] - pairs[1])
        fields.append(sizeoffield)
        sqares.append(pairs)
        pairs = []
#  squares[] have min and max coordinates for iterations, fields[] have size of square
#  divider exists


    for i in range(len(fulls)):
        countdots = 0
        brk = 0
        for j in range(sqares[i][0], sqares[i][2]):
            for k in  range(sqares[i][1],sqares[i][3]):
                if PointInTriangle(k,j,fulls[i][0][1],fulls[i][0][0],fulls[i][1][1],fulls[i][1][0],fulls[i][2][1],fulls[i][2][0]):
                    if lines[j][k] == '1':
                        countdots = countdots + 1
                    elif lines[j][k] == '0':
                        brk = 1
                        break
            if brk:
                brk = 0
                countdots = 0
                break
        if countdots > maxim[0]:
            maxim = []
            maxim.append(countdots)
            maxim.append(fulls[i])
            maxim.append(statement)
            print(maxim)

  #  if len(maxim) <3:
    #  ascending
    fieldssrt = sorted(fields)
      #  print(len(fieldssrt))
  #  else:
      #  fttem = fields.copy()
      #  ftemp = fttem.pop(maxim[2])
      #  fieldssrt = sorted(fttem)
      #  fieldssrt.insert(0,ftemp)




#    print('squares')
#    print(sqares)
#    print('fields')
#    print(fields)
 #   print(fieldssrt)


    lambd = []
    mu = []

    for i in fields:
        z = 1
        for j in fieldssrt:
            if j == i:
                key = (1/2)*(1-((math.cos(math.pi*z/divider))))
                mu.append(key)  #  or key
                lambd.append(1-key)  #  1-key
                break
            else:
                z += 1

    tmptriangles = bfulls.copy()

    ########################################################################################################
    for i in range(len(tmptriangles)):
        for j in range(len(tmptriangles[i])):
            # added to go for every bit
            for k in range(len(tmptriangles[i][j])):
                for l in range(len(tmptriangles[i][j][k])):
            #  going through all individuals and their features
            #  checking for propability to get immigration
                    probs = lambd[i]
                    #print(probs)
                    rand = random.random()
                    if rand < probs:
                #  if propability to migrate is bigger
                #  following actions are made to make roullete wheel work without calculating the current individual
                #  dropping out current individual, because it can't immigrate to itself
                        mu2 = mu.copy()
                        mu2.pop(i)
                        tmptriangles2 = bfulls.copy()
                        tmptriangles2.pop(i)
                #  using roullette wheel to select emigrating individual
                        selected = roulettewheel(mu2)
                #  selecting its feature and passing it to current individual
                        tmptriangles[i][j][k][l] = tmptriangles2[selected][j][k][l]
                #  adding random mutation propability
                        if random.random() < 0.001:
                            tmptriangles[i][j][k][l] = abs(tmptriangles[i][j][k][l] - 1)

    #  passing to another generation

    bfulls = tmptriangles.copy()
    del fulls[:]
    individualsInDecimal = []
    individualsInBinary = []
    for i in range(len(bfulls)):
        for j in range(len(bfulls[i])):
            y = binaryToDecimal(bfulls[i][j][0])
            x = binaryToDecimal(bfulls[i][j][1])
            by = bfulls[i][j][0]
            bx = bfulls[i][j][1]
            while (int(lines[y][x]) == 0):
                bfulls[i][j][0] = createrandomnumber(featNum)
                bfulls[i][j][1] = createrandomnumber(featNum)
                y = binaryToDecimal(bfulls[i][j][0])
                x = binaryToDecimal(bfulls[i][j][1])
                by = bfulls[i][j][0]
                bx = bfulls[i][j][1]

            binoms.append(y)

            binoms.append(x)

            if flg1 == 0:
                flg1 = 1
                trinoms.append(binoms)

            elif flg2 == 0:
                flg2 = 1
                trinoms.append(binoms)

            else:
                trinoms.append(binoms)
                btrinoms.append(bbinoms)
                fulls.append(trinoms)
                trinoms = []
                btrinoms = []
                flg1 = 0
                flg2 = 0
            binoms = []
            bbinoms = []
            ##############################################

    ########################################################################################################
    statement = statement + 1
    #if statement % 1000 == 0:
      #  print('+1k')




sqares = []
pairs = []
fields = []


for i in fulls:
    pairs.append(min(i[0][0], i[1][0], i[2][0]))
    pairs.append(min(i[0][1], i[1][1], i[2][1]))
    pairs.append(max(i[0][0], i[1][0], i[2][0]))
    pairs.append(max(i[0][1], i[1][1], i[2][1]))
    sizeoffield= (pairs[2] - pairs[0]) * (pairs[3] - pairs[1])
    fields.append(sizeoffield)
    sqares.append(pairs)
    pairs = []
#  squares[] have min and max coordinates for iterations, fields[] have size of square
#  divider exists



for i in range(len(fulls)):
    countdots = 0
    brk = 0
    for j in range(sqares[i][0], sqares[i][2]):
        for k in  range(sqares[i][1],sqares[i][3]):
            if PointInTriangle(k,j,fulls[i][0][1],fulls[i][0][0],fulls[i][1][1],fulls[i][1][0],fulls[i][2][1],fulls[i][2][0]):
                if lines[j][k] == '1':
                    countdots = countdots + 1
                elif lines[j][k] == '0':
                    brk = 1
                    break
        if brk:
            brk = 0
            countdots = 0
            break
    if countdots > maxim[0]:
        maxim = []
        maxim.append(countdots)
        maxim.append(fulls[i])
        maxim.append(i)
        maxim.append(statement)
        print(maxim)



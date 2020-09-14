#  IMPROTERS
import random

#  END OF IMPORTS

#  INSERT FUNCTIONS


def binaryToDecimal(x):
    value = 0
    t = x.copy()
    for i in range(len(t)):
        digit = t.pop()
        if digit == 1:
            value = value + pow(2, i)
    return value

def equation(y):
#  Apply eqation for search of max
#  already known to be possible to give negative power
    result = pow(y, 2)
#  possible results:
#  pow(y, x) x is possitive
#  pow(y, -x) must avoid divsion by 0 by alternating equationbyzero function
#  (-y*y +x) x is any int including 0
    return result


def eqiationifzero(y):
    result = y
#  results: |||| alternatives for results:
#  pow(y, x) x is possitive |||| y
#  pow(y, -x) x is possitive |||| y
#  (-y*y +x) x is any int including 0 |||| (y+x) x is any int including 0
    return result


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


#  INSERTION OF FUNCTIONS ENDS
#  Get number of individuals and number of features with a default of 4 and 5
try:
    indNum = int(input("Enter number of individuals: "))
except ValueError as err:
    print("error:")
    print(err)
    print("setting individuals number to default")
    indNum = 10
try:
    featNum = int(input("Enter number of features: "))
except ValueError as err:
    print("error:")
    print(err)
    print("setting features number to default")
    featNum = 5

divider = indNum + 1

print("Number of individuals:", indNum, "Number of features:", featNum)

#  generate sequences of 0 and 1 for individuals
individualsInBinary = []
for i in range(indNum):
    tempr = []
    for j in range(featNum):
        temp2 = random.randint(0, 1)
        tempr.append(temp2)
    individualsInBinary.append(tempr)
print(individualsInBinary)


individualsInDecimal = []
individualsPowered = []


for x in individualsInBinary:
    val = binaryToDecimal(x)
    individualsInDecimal.append(val)
    if val != 0:
        individualsPowered.append(equation(val))
    else:
        individualsPowered.append(eqiationifzero(val))
print(individualsPowered)

theFirstBinary = individualsInBinary.copy()
statement = 0
while statement < 60000:

    #  ############################## CONVERT TO DECIMAL, COUNT POWERED
    individualsInDecimal = []
    individualsPowered = []

    for x in individualsInBinary:
        val = binaryToDecimal(x)
        individualsInDecimal.append(val)
        if val != 0:
            individualsPowered.append(equation(val))
        else:
            individualsPowered.append(eqiationifzero(val))

    #  print(individualsInDecimal)
    poweredSorted = sorted(individualsPowered)

    #  print("powered", individualsPowered)
    #  print("sorted", poweredSorted)
    #  ###############################
    #  calculate mu and lambda values

    lambd = []
    mu = []

    for i in individualsPowered:
        z = 1
        for j in poweredSorted:
            if j == i:
                key = z/divider
                mu.append(key)  #  or key
                lambd.append(1-key)  #  1-key
                break
            else:
                z += 1

    #    print("lambda", lambd)
    #    print("mu", mu)
    #    print("results")
    #    print(individualsInBinary)
    temporaryIndividuals = individualsInBinary.copy()

    for i in range(len(temporaryIndividuals)):
        for j in range(len(temporaryIndividuals[i])):
            #  going through all individuals and their features
            #  checking for propability to get immigration
            probs = lambd[i]
            rand = random.random()
            if rand < probs:
                #  if propability to migrate is bigger
                #  following actions are made to make roullete wheel work without calculating the current individual
                #  dropping out current individual, because it can't immigrate to itself
                mu2 = mu.copy()
                mu2.pop(i)
                temporaryIndividuals2 = individualsInBinary.copy()
                temporaryIndividuals2.pop(i)
                #  using roullette wheel to select emigrating individual
                selected = roulettewheel(mu2)
                #  selecting its feature and passing it to current individual
                temporaryIndividuals[i][j] = temporaryIndividuals2[selected][j]
                #  adding random mutation propability
                if random.random() < 0.001:
                    temporaryIndividuals[i][j] = abs(temporaryIndividuals[i][j] - 1)
    #  passing to another generation
    individualsInBinary = temporaryIndividuals.copy()

    statement += 1

#  additional calculations to get the result
individualsInDecimal = []
individualsPowered = []


for x in individualsInBinary:
    val = binaryToDecimal(x)
    individualsInDecimal.append(val)
    if val != 0:
        individualsPowered.append(equation(val))
    else:
        individualsPowered.append(eqiationifzero(val))
print(individualsInBinary)
print(individualsPowered)
print(max(individualsPowered))

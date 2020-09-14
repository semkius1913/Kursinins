filename = "inout/pic2.txt"
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

counter = 0
y1 = 52
y2 = 170
x1 = 52
x2 = 133
for i in range(y1,y2):
    for j in range(x1,x2):
        if lines[i][j] == '1':
            counter +=1
print(counter)

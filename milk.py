"""
ID: alex.go2
LANG: PYTHON3
TASK: milk
"""
totalcost = 0


f = open('milk.in', 'r')
g = open('milk.out', 'w')
readfile = f.readlines()
gallonsneeded = int(readfile[0].split(" ")[0])
numfarmers = int(readfile[0].split(" ")[1])
arr = []
for x in range (1, numfarmers + 1):
        arr.append([int(readfile[x].split(" ")[0]),int(readfile[x].split(" ")[1]) ])

while gallonsneeded != 0:
    smallestnum = arr[0][0]
    whichone = 0
    for x in range(0, len(arr)):
        if arr[x][0] < smallestnum:
            smallestnum = arr[x][0]
            whichone = x
  
    if gallonsneeded > arr[whichone][1]:
        gallonsneeded = gallonsneeded - arr[whichone][1]
        totalcost = totalcost + arr[whichone][0] * arr[whichone][1]
    
        arr.pop(whichone)
    else:
        totalcost = totalcost + gallonsneeded * arr[whichone][0]
        gallonsneeded = 0
g.write(str(totalcost) + "\n")
g.close()

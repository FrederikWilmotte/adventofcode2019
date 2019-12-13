# Advent10 - Part1
# Day 10: Monitoring Station

#Bestand met de map van asteroiden inladen in het geheugen (aMap)
bestandMap = open("Day10map.txt","r")
rij = []
for lijn in bestandMap:
    lijn = lijn.rstrip("\n")
    rij.append(lijn)
aMap = [[0 for x in range(len(lijn))] for y in range(len(rij))]

for r in range(len(rij)):
    for k in range(len(lijn)):
        aMap[r][k]=rij[r][k:k+1]
rijen = len(rij)
kolommen = len(lijn)
print(rijen)
print(kolommen)
print(aMap[4][0])
print(aMap[0][4])
# Advent6 - Part2
# Day 6: Universal Orbit Map
orbits = []
objectA = []
objectB = []
wegNaarCOMYOU = []
wegNaarCOMSAN = []
objectYOU = "YOU"
objectSAN = "SAN"
objectCOM = "COM"
objectSEARCH = ""
orbitmap = open("Day6map.txt","r")
afstand = 0
#Laden van orbits is het geheugen
for orbit in orbitmap:
    orbits.append(orbit)
    objectA.append(orbit[:3])
    objectB.append(orbit[4:7])
#Bepalen van de afstand van YOU tot COM
objectSEARCH = objectYOU
while objectSEARCH != objectCOM:
    gevonden = "nee"
    i = 0
    while i < len(orbits) and gevonden == "nee":
        if objectB[i] == objectSEARCH:
          gevonden = "ja"
          wegNaarCOMYOU.append(objectA[i])
          objectSEARCH = objectA[i]
        i = i + 1
#Bepalen van de afstand van YOU tot SAN
objectSEARCH = objectSAN
while objectSEARCH != objectCOM:
    gevonden = "nee"
    i = 0
    while i < len(orbits) and gevonden == "nee":
        if objectB[i] == objectSEARCH:
          gevonden = "ja"
          wegNaarCOMSAN.append(objectA[i])
          objectSEARCH = objectA[i]
        i = i + 1
#Bepalen gemeenschappelijke orbiter
gevonden = "nee"
i = 0
while i < len(wegNaarCOMYOU) and gevonden == "nee":
    j = 0
    while j < len(wegNaarCOMSAN) and gevonden == "nee":
        if wegNaarCOMYOU[i] == wegNaarCOMSAN[j]:
            afstand = i + j
            gevonden = "ja"
        j = j + 1
    i = i + 1
print("Afstand",afstand)
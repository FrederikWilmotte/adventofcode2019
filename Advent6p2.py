# Advent6 - Part2
# Day 6: Universal Orbit Map

#Bepalen van de afstand tot object COM
def orbit_afstand(objectSEARCH):
    global orbit_stappen
    orbit_stappen = []
    while objectSEARCH != "COM":
        gevonden = "nee"
        i = 0
        while i < len(objectA) and gevonden == "nee":
            if objectB[i] == objectSEARCH:
                gevonden = "ja"
                orbit_stappen.append(objectA[i])
                objectSEARCH = objectA[i]
            i = i + 1
    return orbit_stappen

#declaraties
objectA = []
objectB = []
wegNaarCOMYOU = []
wegNaarCOMSAN = []
orbitmap = open("Day6map.txt","r")

#Laden van orbits is het geheugen
for orbit in orbitmap:
    objectA.append(orbit[:3])
    objectB.append(orbit[4:7])

#Bepalen van de afstand van YOU tot COM
orbit_afstand("YOU")
wegNaarCOMYOU = orbit_stappen

#Bepalen van de afstand van YOU tot SAN
orbit_afstand("SAN")
wegNaarCOMSAN = orbit_stappen

#Bepalen van de kortste afstand tot het gemeenschappelijke object
gevonden = "nee"
afstand = 0
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
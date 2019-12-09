# Advent6 - Part1
# Day 6: Universal Orbit Map
objectA = []
objectB = []
zoekA = []
zoekB = []
aantalorbits = 0
afstand = 0
orbitmap = open("Day6map.txt","r")

#Laden van orbits is het geheugen
for orbit in orbitmap:
    objectA.append(orbit[:3])
    objectB.append(orbit[4:7])

#Zoeken van het aantal orbits vanaf COM
zoekA.append("COM")
while len(zoekA) > 0:
    i = 0
    afstand = afstand + 1
    while i < len(zoekA):
        j = 0
        while j < len(objectA):
            if zoekA[i] == objectA[j]:
                aantalorbits = aantalorbits + (1 * afstand)
                zoekB.append(objectB[j])
            j = j + 1
        i = i + 1
    zoekA.clear()
    zoekA = zoekB.copy()
    zoekB.clear()
print("Aantal orbits",aantalorbits)
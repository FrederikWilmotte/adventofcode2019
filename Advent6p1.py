# Advent6 - Part1
# Day 6: Universal Orbit Map
orbits = []
objectA = []
objectB = []
aantalorbits = 0
afstand = 0
orbitmap = open("Day6map.txt","r")
#Laden van orbits is het geheugen
for orbit in orbitmap:
    orbits.append(orbit)
objectA.append("COM")
while len(objectA) > 0:
    i = 0
    afstand = afstand + 1
    while i < len(objectA):
        #print("objectA",objectA)
        j = 0
        while j < len(orbits):
            string = orbits[j]
            eerste = string[:3]
            tweede = string[4:7]
            #print("Eerste",eerste)
            #print("Tweede",tweede)
            if eerste == objectA[i]:
                aantalorbits = aantalorbits + (1 * afstand)
                #print("Aantal orbits",aantalorbits)
                #print("Tweede",tweede)
                objectB.append(tweede)
            j = j + 1
        i = i + 1
    objectA.clear()
    objectA = objectB.copy()
    objectB.clear()
print("Aantal orbits",aantalorbits)
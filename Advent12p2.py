# Advent12 - Part1
# Day 12: The N-Body Problem

import copy
from math import gcd
from functools import reduce

#Definieer klasse "Moon"
class Moon:
    def __init__(self,x,y,z,velX=0,velY=0,velZ=0):
        self.x = x
        self.y = y
        self.z = z
        self.velX = velX
        self.velY = velY
        self.velZ = velZ

#Definieer 4 objecten van de klasse "Moon"
Io = Moon(4,1,1)
Europa = Moon(11,-18,-1)
Ganymede = Moon(-2,-10,-4)
Callisto = Moon(-7,-2,14)

#Testdata
#Io = Moon(-1,0,2)
#Europa = Moon(2,-10,-7)
#Ganymede = Moon(4,-8,8)
#Callisto = Moon(3,5,-1)

#Sla alle "Moons" op
Moons = []
Moons.append(Io)
Moons.append(Europa)
Moons.append(Ganymede)
Moons.append(Callisto)

#Sla alle originele "Moons" op
originalMoons = copy.copy(Moons)

#Bereken de nieuwe positie en velocity na 1 stap
def berekenGravityVelocity(Moons):
    newMoons = []
    for originalMaan in Moons:
        maan = copy.copy(originalMaan)
        for andereMaan in Moons:
            if originalMaan.x > andereMaan.x:
                maan.velX = maan.velX - 1
            elif originalMaan.x < andereMaan.x:
                maan.velX = maan.velX + 1
            if originalMaan.y > andereMaan.y:
                maan.velY = maan.velY - 1
            elif originalMaan.y < andereMaan.y:
                maan.velY = maan.velY + 1
            if originalMaan.z > andereMaan.z:
                maan.velZ = maan.velZ - 1
            elif originalMaan.z < andereMaan.z:
                maan.velZ = maan.velZ + 1
        newMoons.append(maan)
        maan.x = maan.x + maan.velX
        maan.y = maan.y + maan.velY
        maan.z = maan.z + maan.velZ
    return (newMoons)

#Controleer gelijke coordinaten
def berekenGelijkeCoordinaat(Moons,originalMoons):
    n = 0
    x = True
    y = True
    z = True
    while n < len(Moons):
        if Moons[n].x != originalMoons[n].x or Moons[n].velX != originalMoons[n].velX:
            x = False
        if Moons[n].y != originalMoons[n].y or Moons[n].velY != originalMoons[n].velY:
            y = False
        if Moons[n].z != originalMoons[n].z or Moons[n].velZ != originalMoons[n].velZ:
            z = False
        n = n + 1
    return (x,y,z)

#Berekenen kleinste gemeen veelvoud
def kgv(x, y):
    return x * y // gcd(x, y)

def kgvMeerdere(*nummers): 
    return reduce(kgv, nummers)

alleGevonden = False
xGevonden = False
yGevonden = False
zGevonden = False
teller = 0
while alleGevonden == False:
    Moons = berekenGravityVelocity(Moons)
    (xGelijk,yGelijk,zGelijk) = berekenGelijkeCoordinaat(Moons,originalMoons)
    teller = teller + 1
    if xGelijk == True and xGevonden == False:
        xGevonden = True
        x = teller
    if yGelijk == True and yGevonden == False:
        yGevonden = True
        y = teller
    if zGelijk == True and zGevonden == False:
        zGevonden = True
        z = teller
    if xGevonden == True and yGevonden == True and zGevonden == True:
        alleGevonden = True

print("Aantal iteraties",kgvMeerdere(x,y,z))
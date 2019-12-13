# Advent12 - Part1
# Day 12: The N-Body Problem

import copy

#Definieer klasse "Moon"
class Moon:
    def __init__(self,x,y,z,velX=0,velY=0,velZ=0,step=0):
        self.x = x
        self.y = y
        self.z = z
        self.velX = velX
        self.velY = velY
        self.velZ = velZ
        self.step = step

#Definieer 4 objecten van de klasse "Moon"
Io = Moon(4,1,1)
Europa = Moon(11,-18,-1)
Ganymede = Moon(-2,-10,-4)
Callisto = Moon(-7,-2,14)

#Sla alle "Moons" op
Moons = []
Moons.append(Io)
Moons.append(Europa)
Moons.append(Ganymede)
Moons.append(Callisto)

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

#Bereken Total Energy
def berekenEnergy(Moons):
    totalEnergy = 0
    for maan in Moons:
        pot = abs(maan.x) + abs(maan.y) + abs(maan.z)
        kin = abs(maan.velX) + abs(maan.velY) + abs(maan.velZ)
        totalEnergy = totalEnergy + (pot * kin)
    return totalEnergy

for _ in range(1000):
    Moons = berekenGravityVelocity(Moons)

print("Totale Energie",berekenEnergy(Moons))
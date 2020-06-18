# Advent14 - Part1
# Day 14: Space Stoichiometry

import math

class grondstof:
    def __init__(self, naam, waarde, ingredienten):
        self.naam = naam
        self.waarde = int(waarde)
        self.ingredienten = ingredienten

class ingredient:
    def __init__(self, naam, waarde):
        self.naam = naam
        self.waarde = int(waarde)

def verwerkReactie(reactie, grondstoffen):
    reactie = reactie.split(" => ")
    (naam, waarde) = splitsGrondstof(reactie[1])
    ingredienten = verwerkBenodigdheden(reactie[0])
    grondstoffen.append(grondstof(naam, waarde, ingredienten))

def verwerkBenodigdheden(reactie):
    reactie = reactie.split(",")
    ingredienten = []
    i = 0
    for i in range(len(reactie)):
        (naam, waarde) = splitsGrondstof(reactie[i])
        ingredienten.append(ingredient(naam, waarde))
    return ingredienten

def splitsGrondstof(product):
    product = product.strip()
    delimiter = product.find(" ")
    naam = product[delimiter:]
    waarde = product[:delimiter]
    naam = naam.strip()
    waarde = waarde.strip()
    return naam, waarde

def zoekGrondstof(naam, hoeveelheid):
    factor = 1
    gevonden = False
    for gezochteGrondstof in grondstoffen:
        if naam == gezochteGrondstof.naam:
            factor = math.ceil(hoeveelheid / gezochteGrondstof.waarde)
            gevonden = True
            break
    return gevonden, gezochteGrondstof, factor

# Bestand met de resources inladen
bestandMap = open("Day14input.txt", "r")
reacties = []
for lijn in bestandMap:
    lijn = lijn.rstrip("\n")
    reacties.append(lijn)
    print("lijn",lijn)

# Alle grondstoffen en benodigheden opslaan
grondstoffen = []
for reactie in reacties:
    verwerkReactie(reactie, grondstoffen)

# Zoek FUEL


# Advent4 - Part1
# Day 4: Secure Container
laagste = 273025
hoogste = 767253
wachtwoorden = []
wachtwoord = laagste
while wachtwoord <= hoogste:
    wachtwoord_string = str(wachtwoord)
    wachtwoord_lijst = [wachtwoord_string[0],wachtwoord_string[1],wachtwoord_string[2],wachtwoord_string[3],wachtwoord_string[4],wachtwoord_string[5]]
    positie = 0
    controle_opeen = "nok"
    controle_niet_dalend = "ok"
    while positie < 5:
        #controle 2 opeenvolgende nummers
        if wachtwoord_lijst[positie] == wachtwoord_lijst[positie+1] and controle_niet_dalend == "ok" and controle_opeen == "nok":
            controle_opeen = "ok"
        #controle nummers niet dalend
        if wachtwoord_lijst[positie] > wachtwoord_lijst[positie+1] and controle_niet_dalend == "ok":
            controle_niet_dalend = "nok"
        positie = positie + 1
        #als wachtwoord voldoet aan de ciriteria, toevoegen aan de lijst
    if controle_niet_dalend == "ok" and controle_opeen == "ok":
        wachtwoorden.append(wachtwoord)
    wachtwoord = wachtwoord + 1
print("Aantal mogelijke wachtwoorden:",len(wachtwoorden))
# Advent11 - Part1
# Day 11: Space Police

import sys

def paintingRobot(intcode):
    painted = 0
    pointer = 0
    direction = "up"
    relativeBase = 0
    rij = 1000
    kolom = 1000
    maxRij = 2000
    maxKolom = 2000
    panel = [[0 for x in range(maxRij)] for y in range(maxKolom)]
    panelPainted = [[0 for x in range(maxRij)] for y in range(maxKolom)]
    signalsIn = []
    signalsIn.append(panel[rij][kolom])
    color = 0
    (status,pointer,relativeBase,intcode,signalsOut) = intcodeComputer(pointer,relativeBase,intcode,signalsIn)
    if len(signalsOut) > 0:
        colorNew = signalsOut[0]
        panel[rij][kolom] = colorNew
        panelPainted[rij][kolom] = 1
        (direction,rij,kolom) = facingDirection(direction,signalsOut[1],rij,kolom)
    while status == "waiting":
        signalsIn.clear()
        signalsIn.append(panel[rij][kolom])
        (status,pointer,relativeBase,intcode,signalsOut) = intcodeComputer(pointer,relativeBase,intcode,signalsIn)
        if len(signalsOut) > 0:
            color = signalsOut[0]
            panel[rij][kolom] = color
            panelPainted[rij][kolom] = 1
            (direction,rij,kolom) = facingDirection(direction,signalsOut[1],rij,kolom)
    painted = countPainted(panelPainted,maxRij,maxKolom)
    return painted

def countPainted(panelPainted,maxRij,maxKolom):
    painted = 0
    for rij in range(maxRij):
        for kolom in range(maxKolom):
            if panelPainted[rij][kolom] == 1:
                painted = painted + 1
    return painted

def facingDirection(directionOld,instruction,rij,kolom):
    directionNew = "up"
    if instruction == 0 or instruction == 1:
        if directionOld == "up":
            if instruction == 0:
                directionNew = "left"
            else:
                directionNew = "right"
        elif directionOld == "left":
            if instruction == 0:
                directionNew = "down"
            else:
                directionNew = "up"
        elif directionOld == "down":
            if instruction == 0:
                directionNew = "right"
            else:
                directionNew = "left"
        elif directionOld == "right":
            if instruction == 0:
                directionNew = "up"
            else:
                directionNew = "down"
        else:
            print("Verkeerde richting",directionOld)
            sys.exit(0)
    else:
        print("Verkeerde instructie",instruction)
        sys.exit(0)
    if directionNew == "up":
        rij = rij - 1
    elif directionNew == "right":
        kolom = kolom + 1
    elif directionNew == "down":
        rij = rij + 1
    elif directionNew == "left":
        kolom = kolom - 1
    return (directionNew,rij,kolom)

def intcodeComputer(pointer,relativeBase,intcode,signalsIn):
    status = "run"
    signalsOut = []
    instruction = str(intcode[pointer]).zfill(5)
    (status,pointer,intcode,relativeBase,signalsOut) = verwerkInstruction(status,pointer,instruction,intcode,relativeBase,signalsIn,signalsOut)
    while status == "run":
        instruction = str(intcode[pointer]).zfill(5)
        (status,pointer,intcode,relativeBase,signalsOut) = verwerkInstruction(status,pointer,instruction,intcode,relativeBase,signalsIn,signalsOut)
    return (status,pointer,relativeBase,intcode,signalsOut)

def verwerkInstruction(status,pointer,instruction,intcode,relativeBase,signalsIn,signalsOut):
    (opcode,mode1,mode2,mode3) = readInstruction(instruction)
    if opcode == "01":
        (pointer,intcode) = opcode01(pointer,intcode,relativeBase,mode1,mode2,mode3)
    elif opcode == "02":
        (pointer,intcode) = opcode02(pointer,intcode,relativeBase,mode1,mode2,mode3)
    elif opcode == "03":
        if len(signalsIn) == 0:
            status = "waiting"
        else:
            (pointer,intcode) = opcode03(pointer,intcode,relativeBase,mode1,signalsIn[0])
            signalsIn.pop(0)
    elif opcode == "04":
        (pointer,signalOut) = opcode04(pointer,intcode,relativeBase,mode1)
        signalsOut.append(signalOut)
    elif opcode == "05":
        pointer = opcode05(pointer,intcode,relativeBase,mode1,mode2)
    elif opcode == "06":
        pointer = opcode06(pointer,intcode,relativeBase,mode1,mode2)
    elif opcode == "07":
        (pointer,intcode) = opcode07(pointer,intcode,relativeBase,mode1,mode2,mode3)
    elif opcode == "08":
        (pointer,intcode) = opcode08(pointer,intcode,relativeBase,mode1,mode2,mode3)
    elif opcode == "09":
        (pointer,intcode,relativeBase) = opcode09(pointer,intcode,relativeBase,mode1)
    elif opcode == "99":
        status = "stop"
    else:
        print("Error opcode:",opcode)
        status = "stop"
    return (status,pointer,intcode,relativeBase,signalsOut)

def readInstruction(instruction):
    mode3 = instruction[0]
    mode2 = instruction[1]
    mode1 = instruction[2]
    opcode = instruction[3:]
    return (opcode,mode1,mode2,mode3)

def writeMemory(intcode,positie,waarde):
    if positie >= len(intcode):
        opvullen = positie - len(intcode)
        i = 1
        while i <= opvullen:
            intcode.append(0)
            i = i + 1
        intcode.append(waarde)
    else:
        intcode[positie] = waarde
    return intcode

def readMemory(intcode,positie):
    if positie >= len(intcode):
        opvullen = positie - len(intcode)
        i = 1
        while i <= opvullen:
            intcode.append(0)
            i = i + 1
        intcode.append(0)
    return intcode

def opcode01(pointer,intcode,relativeBase,mode1,mode2,mode3):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    (positie,intcode) = bepaalParam(pointer+3,intcode,relativeBase,mode3,"write")
    intcode=writeMemory(intcode,positie,param1+param2)
    pointer = pointer + 4
    return (pointer,intcode)
        
def opcode02(pointer,intcode,relativeBase,mode1,mode2,mode3):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    (positie,intcode) = bepaalParam(pointer+3,intcode,relativeBase,mode3,"write")
    intcode=writeMemory(intcode,positie,param1*param2)
    pointer = pointer + 4
    return (pointer,intcode)

def opcode03(pointer,intcode,relativeBase,mode1,signalIn):
    (positie,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"write")
    intcode=writeMemory(intcode,positie,signalIn)
    pointer = pointer + 2
    return (pointer,intcode)

def opcode04(pointer,intcode,relativeBase,mode1):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    signalOut = param1
    pointer = pointer + 2
    return (pointer,signalOut)

def opcode05(pointer,intcode,relativeBase,mode1,mode2):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    if param1 != 0:
        pointer = param2
    else:
        pointer = pointer + 3
    return pointer

def opcode06(pointer,intcode,relativeBase,mode1,mode2):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    if param1 == 0:
        pointer = param2
    else:
        pointer = pointer + 3
    return pointer

def opcode07(pointer,intcode,relativeBase,mode1,mode2,mode3):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    (positie,intcode) = bepaalParam(pointer+3,intcode,relativeBase,mode3,"write")
    if param1 < param2:
        intcode=writeMemory(intcode,positie,1)
    else:
        intcode=writeMemory(intcode,positie,0)
    pointer = pointer + 4
    return (pointer,intcode)

def opcode08(pointer,intcode,relativeBase,mode1,mode2,mode3):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    (param2,intcode) = bepaalParam(pointer+2,intcode,relativeBase,mode2,"read")
    (positie,intcode) = bepaalParam(pointer+3,intcode,relativeBase,mode3,"write")
    if param1 == param2:
        intcode=writeMemory(intcode,positie,1)
    else:
        intcode=writeMemory(intcode,positie,0)
    pointer = pointer + 4
    return (pointer,intcode)

def opcode09(pointer,intcode,relativeBase,mode1):
    (param1,intcode) = bepaalParam(pointer+1,intcode,relativeBase,mode1,"read")
    relativeBase = relativeBase + param1
    pointer = pointer + 2
    return (pointer,intcode,relativeBase)

def bepaalParam(pointer,intcode,relativeBase,mode,action):
    if mode == "0":
        param = intcode[pointer]
        if action == "read":
            intcode = readMemory(intcode,param)
            param = intcode[param]
    elif mode == "1":
        param = intcode[pointer]
    elif mode == "2":
        param = intcode[pointer]+relativeBase
        if action == "read":
            intcode = readMemory(intcode,param)
            param = intcode[param]
    else:
        print("Error mode:",mode)
    return (param,intcode)

intcode = [3,8,1005,8,325,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,28,2,3,7,10,2,1109,3,10,2,102,0,10,2,1005,12,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,67,2,109,12,10,1,1003,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,96,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,119,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,141,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,162,1,106,17,10,1006,0,52,1006,0,73,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,194,1006,0,97,1,1004,6,10,1006,0,32,2,8,20,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,231,1,1,15,10,1006,0,21,1,6,17,10,2,1005,8,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,267,2,1007,10,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,294,1006,0,74,2,1003,2,10,1,107,1,10,101,1,9,9,1007,9,1042,10,1005,10,15,99,109,647,104,0,104,1,21101,936333018008,0,1,21101,342,0,0,1106,0,446,21102,937121129228,1,1,21101,0,353,0,1105,1,446,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,209383001255,1,21102,400,1,0,1106,0,446,21101,0,28994371675,1,21101,411,0,0,1105,1,446,3,10,104,0,104,0,3,10,104,0,104,0,21101,867961824000,0,1,21101,0,434,0,1106,0,446,21102,1,983925674344,1,21101,0,445,0,1106,0,446,99,109,2,21201,-1,0,1,21102,40,1,2,21101,477,0,3,21102,467,1,0,1106,0,510,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,472,473,488,4,0,1001,472,1,472,108,4,472,10,1006,10,504,1101,0,0,472,109,-2,2106,0,0,0,109,4,1201,-1,0,509,1207,-3,0,10,1006,10,527,21102,1,0,-3,21202,-3,1,1,21201,-2,0,2,21102,1,1,3,21102,1,546,0,1106,0,551,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,574,2207,-4,-2,10,1006,10,574,22101,0,-4,-4,1105,1,642,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,0,593,0,1105,1,551,22102,1,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,612,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,634,21201,-1,0,1,21101,634,0,0,105,1,509,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]
painted = paintingRobot(intcode)
print("Painted",painted)
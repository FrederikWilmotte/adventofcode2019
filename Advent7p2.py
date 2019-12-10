# Advent7 - Part2
# Day 7: Amplification Circuit

from itertools import permutations

def bepaalAllePhases(minPhase,maxPhase):
    phases = []
    for phase in range(minPhase,maxPhase+1):
        phases.append(phase)
    allePhases = permutations(phases)
    return allePhases

def thruster(phases,intcode):
    statusAmp = []
    intcodeMem = []
    pointerMem = []
    signalOut = 0
    maxAmpNr = 0
    for phase in phases:
        pointerMem.append(0)
        statusAmp.append("run")
        intcodeMem.append(intcode)
        (status,signalOut,intcodeMem[maxAmpNr],pointerMem[maxAmpNr]) = amplifier(statusAmp[maxAmpNr],phase,signalOut,intcodeMem[maxAmpNr],pointerMem[maxAmpNr])
        statusAmp[maxAmpNr] = status
        maxAmpNr = maxAmpNr + 1
    while status != "stop":
        for ampNr in range(0,maxAmpNr):
            (status,signalOut,intcodeMem[ampNr],pointerMem[ampNr]) = amplifier(statusAmp[ampNr],0,signalOut,intcodeMem[ampNr],pointerMem[ampNr])
            statusAmp[ampNr] = status
    return signalOut

def amplifier(status,phase,signalIn,intcode,pointer):
    signalsIn = []
    if status == "run":
        signalsIn.append(phase)
    signalsIn.append(signalIn)
    (status,signalOut,intcode,pointer) = intcodeComputer(pointer,intcode,signalsIn)
    return (status,signalOut,intcode,pointer)

def intcodeComputer (pointer,intcode,signalsIn):
    status = "run"
    signalOut = 0
    instruction = str(intcode[pointer]).zfill(5)
    (status,pointer,intcode,signalsIn,signalOut) = verwerkInstruction(status,pointer,instruction,intcode,signalsIn,signalOut)
    while status == "run":
        instruction = str(intcode[pointer]).zfill(5)
        (status,pointer,intcode,signalsIn,signalOut) = verwerkInstruction(status,pointer,instruction,intcode,signalsIn,signalOut)
    return (status,signalOut,intcode,pointer)

def verwerkInstruction(status,pointer,instruction,intcode,signalsIn,signalOut):
    (opcode,mode1,mode2,mode3) = readInstruction(instruction)
    if opcode == "01":
        (pointer,intcode) = opcode01(pointer,intcode,mode1,mode2)
    elif opcode == "02":
        (pointer,intcode) = opcode02(pointer,intcode,mode1,mode2)
    elif opcode == "03":
        if len(signalsIn) == 0:
            status = "waiting"
        else:
            (pointer,intcode) = opcode03(pointer,intcode,signalsIn[0])
            signalsIn.pop(0)
    elif opcode == "04":
        (pointer,signalOut) = opcode04(pointer,intcode)
    elif opcode == "05":
        pointer = opcode05(pointer,intcode,mode1,mode2)
    elif opcode == "06":
        pointer = opcode06(pointer,intcode,mode1,mode2)
    elif opcode == "07":
        (pointer,intcode) = opcode07(pointer,intcode,mode1,mode2)
    elif opcode == "08":
        (pointer,intcode) = opcode08(pointer,intcode,mode1,mode2)
    elif opcode == "99":
        status = "stop"
    else:
        print("Error opcode:",opcode)
        status = "stop"
    return (status,pointer,intcode,signalsIn,signalOut)

def readInstruction(instruction):
    mode3 = instruction[0]
    mode2 = instruction[1]
    mode1 = instruction[2]
    opcode = instruction[3:]
    return (opcode,mode1,mode2,mode3)

def opcode01(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    positie = intcode[pointer+3]
    intcode[positie]=param1+param2
    pointer = pointer + 4
    return (pointer,intcode)
        
def opcode02(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    positie = intcode[pointer+3]
    intcode[positie]=param1*param2
    pointer = pointer + 4
    return (pointer,intcode)

def opcode03(pointer,intcode,signalIn):
    positie = intcode[pointer+1]
    intcode[positie] = signalIn
    pointer = pointer + 2
    return (pointer,intcode)

def opcode04(pointer,intcode):
    positie = intcode[pointer+1]
    signalOut = intcode[positie]
    pointer = pointer + 2
    return (pointer,signalOut)

def opcode05(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    if param1 != 0:
        pointer = param2
    else:
        pointer = pointer + 3
    return pointer

def opcode06(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    if param1 == 0:
        pointer = param2
    else:
        pointer = pointer + 3
    return pointer

def opcode07(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    positie = intcode[pointer+3]
    if param1 < param2:
        intcode[positie]=1
    else:
        intcode[positie]=0
    pointer = pointer + 4
    return (pointer,intcode)

def opcode08(pointer,intcode,mode1,mode2):
    param1 = bepaalParam(pointer+1,intcode,mode1)
    param2 = bepaalParam(pointer+2,intcode,mode2)
    positie = intcode[pointer+3]
    if param1 == param2:
        intcode[positie]=1
    else:
        intcode[positie]=0
    pointer = pointer + 4
    return (pointer,intcode)

def bepaalParam(pointer,intcode,mode):
    param = intcode[pointer]
    if mode  == "0":
        param = intcode[param]
    return param

intcode = [3,8,1001,8,10,8,105,1,0,0,21,38,63,76,93,118,199,280,361,442,99999,3,9,101,3,9,9,102,3,9,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,1002,9,5,9,101,5,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,1002,9,5,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99]
minPhase = 5
maxPhase = 9
maxThruster = 0

for phases in bepaalAllePhases(minPhase,maxPhase):
    signalOut = thruster(phases,intcode)
    if signalOut > maxThruster:
        maxThruster = signalOut
print("Max Thruster",maxThruster)
# Advent7 - Part2
# Day 7: Amplification Circuit

def intcodeComputer (intcode,inputsignals):
    address = 0
    signals = 0
    oppcode = str(intcode[address]).zfill(5)
    #A = oppcode[0]
    B = oppcode[1]
    C = oppcode[2]
    DE = oppcode[3:]
    while DE != "99":
        print("Instructie",oppcode)
        if DE == "01" or DE == "02" or DE == "05" or DE == "06" or DE == "07" or DE == "08":
            param1 = intcode[address+1]
            param2 = intcode[address+2]
            if B == "0":
                param2 = intcode[param2]
            if C == "0":
                param1 = intcode[param1]
            if DE == "01":
                param3 = intcode[address+3]
                intcode[param3]=param1+param2
                address = address + 4
            if DE == "02":
                param3 = intcode[address+3]
                intcode[param3]=param1*param2
                address = address + 4
            if DE == "05":
                if param1 != 0:
                    address = param2
                else:
                    address = address + 3
            if DE == "06":
                if param1 == 0:
                    address = param2
                else:
                    address = address + 3
            if DE == "07":
                param3 = intcode[address+3]
                if param1 < param2:
                    intcode[param3]=1
                else:
                    intcode[param3]=0
                address = address + 4
            if DE == "08":
                param3 = intcode[address+3]
                if param1 == param2:
                    intcode[param3]=1
                else:
                    intcode[param3]=0
                address = address + 4
        elif DE == "03" or DE == "04":
            param1 = intcode[address+1]
            if DE == "03":
                intcode[param1] = inputsignals[signals]
                signals = signals + 1
            else:
                outputsignal = intcode[param1]
            address = address + 2
        elif DE == "99":
            break
        else:
            print("Error DE:",DE)
            break
        oppcode = str(intcode[address]).zfill(5)
        A = oppcode[0]
        B = oppcode[1]
        C = oppcode[2]
        DE = oppcode[3:]
        #print(intcode)
    return outputsignal

intcode = [3,8,1001,8,10,8,105,1,0,0,21,38,63,76,93,118,199,280,361,442,99999,3,9,101,3,9,9,102,3,9,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,1002,9,5,9,101,5,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,1002,9,5,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99]
signals = []

p1 = 5
thruster = 0
while p1 < 10:
    p2 = 5
    while p2 < 10:
        if p2 == p1:
            p2 = p2 + 1
        else:
            p3 = 5
            while p3 < 10:
                if p3 == p2 or p3 == p1:
                    p3 = p3 + 1
                else:
                    p4 = 5
                    while p4 < 10:
                        if p4 == p3 or p4 == p2 or p4 == p1:
                            p4 = p4 + 1
                        else:
                            p5 = 5
                            while p5 < 10:
                                if p5 == p4 or p5 == p3 or p5 == p2 or p5 == p1:
                                    p5 = p5 + 1
                                else:
                                    signals = [p1,0]
                                    amp1 = intcodeComputer(intcode,signals)
                                    signals = [p2,amp1]
                                    amp2 = intcodeComputer(intcode,signals)
                                    signals = [p3,amp2]
                                    amp3 = intcodeComputer(intcode,signals)
                                    signals = [p4,amp3]
                                    amp4 = intcodeComputer(intcode,signals)
                                    signals = [p5,amp4]
                                    amp5 = intcodeComputer(intcode,signals)
                                    if amp5 > thruster:
                                        thruster = amp5
                                    p5 = p5 + 1
                            p4 = p4 + 1
                    p3 = p3 + 1
            p2 = p2 + 1
    p1 = p1 + 1
print("Max Thruster",thruster)
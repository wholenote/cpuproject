instructions_dict = {
    "halt" : "0",
    "irmovq" : "1",
    "rrmovq" : "2",
    "ldm" : "3",
    "ldr" : "4",
    "stm" : "5",
    "str" : "6",
    "add" : "7",
    "sub" : "8",
    "mul" : "9",
    "jmp" : "A",
    "jz" : "B",
    "r0" : "0",
    "r1" : "1",
    "r2" : "2",
    "r3" : "3",
    "r4" : "4",
    "r5" : "5",
    "r6" : "6",
    "r7" : "7"
}


with open('rom', 'w') as romfile:
    romfile.write('v2.0 raw\n')
    with open('main.txt', 'r') as assemblyfile:
        instructions = assemblyfile.read().split('\n')
        for instruction in instructions:
            instruction_split_up = instruction.split(' ')
            try:
                romfile.write(instructions_dict[instruction[0]])
                romfile.write('\n')
                romfile.write(instructions_dict[instruction[1]])
            except:
                if instruction[0]:
                else:
                    print("error")
            print(instruction_split_up)
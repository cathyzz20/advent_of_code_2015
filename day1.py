#part 1
with open('input_text_1.txt', 'r') as file:
    instruction_set=file.read()
floor=0
for instruction in instruction_set:
    if instruction == "(":
        floor = floor +1
    elif instruction == ")":
        floor = floor-1
print("Santa is at floor: {}".format(floor))
#part2

instruction_number=1
for instruction in instruction_set:
    if instruction == "(":
        floor = floor +1
    elif instruction == ")":
        floor = floor-1
    if floor==-1:
        print("Santa first entered the basement at the position:{}".format(instruction_number))
        break
    instruction_number+=1
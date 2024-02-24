#part1
with open('input_text_3.txt', 'r') as file:
    path_houses=file.read()
house_list=[]
x=0
y=0
for ind, i in enumerate(path_houses):
    point = path_houses[ind]
    if point == '^':
        y+=1
    elif point == 'v':
        y-=1
    elif point == '>':
        x+=1
    else:
        x-=1
    future_position=(x,y)
    house_list.append(future_position)
print(f'Part one answer : {len(set(house_list))+1}') 

#part2
santa_path=[]
robot_path=[]
for ind, i in enumerate(path_houses):
    if ind%2==0:
        santa_path.append(i)
    else:
        robot_path.append(i)
def move(lst):
    house_list2=[]
    x=0
    y=0
    for i in lst:
        if i == '^':
            y+=1
        elif i == 'v':
            y-=1
        elif i == '>':
            x+=1
        else:
            x-=1
        future_position2=(x,y)
        house_list2.append(future_position2)
    return house_list2
robot_houses=move(santa_path)
santa_houses=move(robot_path)
total_houses=set(robot_houses+santa_houses)
print(f'Part two answer : {len(total_houses)}')





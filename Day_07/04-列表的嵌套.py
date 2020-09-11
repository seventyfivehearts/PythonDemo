import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)

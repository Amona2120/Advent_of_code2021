coordinate_x = 0
coordinate_y = 0
aim = 0
try:
    while True:
        line = input()
        new_line = line.split()
        direction = new_line[0]
        value = int(new_line[1])
        if direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        elif direction == "forward":
            coordinate_x += value
            coordinate_y += aim * value
except EOFError:
    print(coordinate_x * coordinate_y)
    
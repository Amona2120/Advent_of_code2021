coordinate_x = 0
coordinate_y = 0
try:
    while True:
        line = input()
        new_line = line.split()
        direction = new_line[0]
        value = int(new_line[1])
        if direction == "forward":
            coordinate_x += value
        elif direction == "up":
            coordinate_y += value
        else:
            coordinate_y -= value
except EOFError:
    coordinate_y = abs(coordinate_y)
    print(coordinate_x * coordinate_y)
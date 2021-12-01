number = 0
second_line = 1000000000
third_line = 1000000000
last_summ = 100000000000000000000000000000000000
try:
    while True:
        line = int(input())
        summ = line + second_line + third_line
        if summ > last_summ:
            number += 1
        third_line = second_line
        second_line = line
        last_summ = summ
except EOFError:
    print(number)

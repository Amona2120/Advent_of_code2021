from input import read_input

def _most_frequent_bit(column):
    if column.count("0") <= column.count("1"):
        return "1"
    else:
        return "0"

def _most_rare_bit(column):
    if column.count("0") <= column.count("1"):
        return "0"
    else:
        return "1"


input_list, bit_len = read_input()

def solve(bit_len, input_list, freq_func):
    for i in range(0, bit_len):
        transposed_list = [[row[bit] for row in input_list] for bit in range(0, bit_len)]
        most_frequent_bit = freq_func(transposed_list[i])
        input_list = [item for item in input_list if item[i] == most_frequent_bit]
        if len(input_list) == 1:
            return int(input_list[0], 2)

a = solve(bit_len, input_list, _most_frequent_bit)
b = solve(bit_len, input_list, _most_rare_bit)
print(a * b)

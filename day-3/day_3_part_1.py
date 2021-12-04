from input import read_input

input_list, bit_len = read_input()
new_list = [[row[bit] for row in input_list] for bit in range(0, bit_len)]
binary_number = []
for item in new_list:
    if item.count("0") > item.count("1"):
        binary_number.append("0")
    else:
        binary_number.append("1")
gamma = ("".join(binary_number))
epsilon = "".join(["0" if bit == "1" else "1" for bit in gamma])
print(int(gamma, 2) * int(epsilon, 2))

def read_input():
    try:
        the_list = []
        while True:
            line = input()
            length =  len(line)
            the_list.append(line)
    except EOFError:
        return the_list, length

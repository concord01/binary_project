def converter(input):
    output = [0,0,0,0]
    while input >= 8:
        input = input - 8
        output[0] = 1
    while input >= 4:
        input = input - 4
        output[1] = 1
    while input >= 2:
        input = input - 2
        output[2] = 1
    while input >= 1:
        input = input - 1
        output[3] = 1
    return output
print(converter(1))
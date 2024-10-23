def converter(input):
    output = []
    index = 0
    inputChange = input
    indexFinal = 0
    # getting array to correct size
    while True:
        if (inputChange - (2 ** index) >= 0):
            index = index + 1
            output.append(0)
        else:
            indexFinal = index
            break
    # correcting the index
    index = 0
    indexFinal = indexFinal-1
    print(inputChange)
    # going and adding adding the 1s into the right spot
    while indexFinal >= 0:
        # decides if it should add a 1 or not to a given index
        if (inputChange - (2 ** indexFinal) >= 0):
            output[index] = 1
            index = index + 1
            inputChange = inputChange - (2 ** indexFinal)
            print(inputChange)
            indexFinal = indexFinal - 1
        else:
            # skips index
            index = index + 1
            indexFinal = indexFinal - 1
    return output
        
    



print(converter(1985))
import constants


def dumpNonogramArray(array):
    string = ""
    for row in array:
        for cell in row:
            if cell:
                string += constants.BLOCK_CHAR
            else:
                string += constants.EMPTY_CHAR
        string += "\n"
    return string.strip()


def flattenArray(array):
    return [b for a in array for b in a]


def transposeArray(array):
    transposedArray = []
    for i in range(len(array[0])):
        transposedArray.append([row[i] for row in array])

    return transposedArray


def dumpRowString(rowNumbers):
    return "\n".join(["".join(row) for row in rowNumbers])

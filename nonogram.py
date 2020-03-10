import os
import re

import constants
import util


def getNonogramInput(nonogramInputPath=None):
    if nonogramInputPath is None:
        nonogramInputPath = input(
            "Enter your input file (has to consist of spaces, newlines and x characters): "
        )

    if not os.path.isfile(nonogramInputPath):
        print("Invalid path")
        getNonogramInput()
        return

    with open(nonogramInputPath, "r") as file:
        nonogramString = file.read()

    # if any character but the listed ones are found
    illegalCharsInText = re.match(
        r"[^" + constants.FILE_BLOCK_CHAR + constants.FILE_EMPTY_CHAR + r"\n]",
        nonogramString,
        re.IGNORECASE
    )

    if illegalCharsInText is not None:
        print("Invalid characters in input (can only contain spaces, newlines and x characters)")
        getNonogramInput()
        return

    return nonogramString


def trimRows(nonogramArray):
    # trim empty rows at the beginning and end
    while len(nonogramArray[0]) == 0:
        nonogramArray.pop(0)
    while len(nonogramArray[-1]) == 0:
        nonogramArray.pop()

    return nonogramArray


def trimColumns(nonogramArray):
    # trim empty cols at the beginning and end
    firstColEmpty = True not in [row[0] for row in nonogramArray]
    lastColEmpty = True not in [row[-1] for row in nonogramArray]

    # no need to go though the loop if nothing is empty
    if firstColEmpty or lastColEmpty:
        for row in nonogramArray:
            if firstColEmpty:
                del row[0]
            if lastColEmpty:
                del row[-1]
        return trimColumns(nonogramArray)  # iterate until all columns have been trimmed
    else:
        return nonogramArray


def normalizeLength(nonogramArray):
    maxRowLength = max([len(line) for line in nonogramArray])

    # append False to row if the whitespace has been trimmed for some reason
    [
        nonogramArray[row].extend(
            [False for d in range(maxRowLength - len(nonogramArray[row]))]
        )
        for row in range(len(nonogramArray))
        if len(nonogramArray[row]) < maxRowLength
    ]

    return nonogramArray


def parseNonogramToArray(nonogramString, trimEmpty=True):

    nonogramArray = [
        [char.lower() == constants.FILE_BLOCK_CHAR for char in line]
        for line in nonogramString.split("\n")
    ]

    nonogramArray = normalizeLength(nonogramArray)

    if trimEmpty:
        nonogramArray = trimRows(nonogramArray)
        nonogramArray = trimColumns(nonogramArray)

    return nonogramArray


def generateRowNumbers(nonogramArray):
    nonogramString = util.dumpNonogramArray(nonogramArray)
    numbers = []
    for row in nonogramString.split("\n"):
        rowNumbers = [len(n) for n in row.split(constants.FILE_EMPTY_CHAR) if n]  # filter empty values
        numbers.append(rowNumbers)
    return numbers


def generateColNumbers(nonogramArray):
    return generateRowNumbers(util.transposeArray(nonogramArray))

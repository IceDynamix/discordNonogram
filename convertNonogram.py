import nonogram
from constants import *
import util


def nonogramEmojiString(nonogramString=None, trimEmpty=True):
    nonogramEmojiString = []  # lines of strings that will be concatenated later with a newline

    nonogramArray = nonogram.parseNonogramToArray(nonogramString, trimEmpty)

    if len(nonogramArray) == 0:
        print("...What's the point of printing an empty nonogram?")
        return

    rowNumbers = nonogram.generateRowNumbers(nonogramArray)
    colNumbers = nonogram.generateColNumbers(nonogramArray)

    # can't display numbers larger than 14 (see py)
    if max(util.flattenArray(rowNumbers)) > 14 or max(util.flattenArray(colNumbers)) > 14:
        print("Sorry, can't print numbers with more than 1 digit...")
        return

    rowNumbersStringArray = rowNumbersString(rowNumbers)
    colNumbersStringArray = colNumbersString(colNumbers)
    playfieldValuesStringArray = playfieldValuesString(nonogramArray)

    maxRowLength = max([len(row) for row in rowNumbers])

    for row in colNumbersStringArray:
        rowString = ""
        for i in range(maxRowLength):
            rowString += EMOJI_EMPTY_CHAR
        rowString += "".join(row)
        nonogramEmojiString.append(rowString)

    for i, row in enumerate(rowNumbersStringArray):
        nonogramEmojiString.append("".join(row + playfieldValuesStringArray[i]))

    finalString = "\n".join(nonogramEmojiString)

    if len(finalString) > DISCORD_MAX_CHARS:
        print(f"The length of the string exceeds the Discord character limit! ({len(finalString)}/{DISCORD_MAX_CHARS})")

    return finalString


def rowNumbersString(rowNumbers):
    maxRowLength = max([len(row) for row in rowNumbers])
    allRowsArray = []
    for row in rowNumbers:
        rowArray = []
        if len(row) < maxRowLength:
            for i in range(maxRowLength - len(row)):
                rowArray.append(EMOJI_EMPTY_CHAR)
        for number in row:
            rowArray.append(EMOJI_NUMBERS[number])
        allRowsArray.append(rowArray)
    return allRowsArray


def colNumbersString(colNumbers):
    return util.transposeArray(rowNumbersString(colNumbers))


def playfieldValuesString(nonogramArray):
    return [
        [
            f"||{EMOJI_BLOCK_CHAR}||" if value
            else f"||{EMOJI_X_CHAR}||"
            for value in row
        ]
        for row in nonogramArray
    ]

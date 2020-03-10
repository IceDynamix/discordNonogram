import nonogram
import convertNonogram

inputFilePath = "input.txt"
outputFilePath = "output.txt"

nonogramString = nonogram.getNonogramInput(inputFilePath)

with open(outputFilePath, "w+") as file:
    file.write(convertNonogram.nonogramEmojiString(nonogramString, trimEmpty=True))

print(f"Successfully written to {outputFilePath}")

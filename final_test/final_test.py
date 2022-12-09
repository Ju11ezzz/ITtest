def printResult(rowNumber, countWords, countSymbols):
    print("В рядку №" + str(rowNumber) + " кількість слів: " + str(countWords)
          + ", кількість символів: " + str(countSymbols))


def countWords(str):
    if len(str.replace("\n", "")) == 0:
        return 0
    words = str.split(" ")
    return len(words)


file = open("files/file.txt", "r")
rowNum = 1
for line in file:
    cntWords = countWords(line)
    printResult(rowNum, cntWords, len(line.replace("\n", "")))
    rowNum += 1

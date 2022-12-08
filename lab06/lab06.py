def getFile(numberGroup):
    fileName = "files/list_" + str(numberGroup) + ".txt"
    file = open(fileName, "r")
    return (file)


def printGroup(numberGroup):
    print("Учні, які ідуть на степендію 'Комп'ютерна інженерія' 1 курс")
    file = getFile(numberGroup)
    print(file.read())


def checkStudent(numberGroup, name):
    file = getFile(numberGroup)
    count = 0
    for line in file:
        if name in line:
            print(line.replace("\n", "") + " - входить у список учнів, які ідуть на степендію.")
            count += 1
    if count == 0:
        print(name + " - не входить у список учнів, які ідуть на степендію.")


while True:
    action = input("Виберіть режим роботи: \n"
                   "1 - виведення списку студентів групи\n"
                   "2 - пошук студентів по імені та номеру групи\n"
                   "q - вихід\n")
    if action == "q":
        print("Дякую за використання нашого програмного продукту!")
        break
    numberGroup = int(input("Введіть номер групи: "))
    while numberGroup < 1 or numberGroup > 3:
        print("-----------------------------")
        print("Такої групи не існує. ")
        numberGroup = int(input("Введіть номер групи: "))
    if action == "1":
        printGroup(numberGroup)
        print("-----------------------------")
    elif action == "2":
        name = input("Введіть ім'я та прізвище: ")
        checkStudent(numberGroup, name)
        print("-----------------------------")

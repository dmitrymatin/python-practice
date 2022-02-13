from random import randrange


def main():
    intervalMinimun = -100
    intervalMaximum = 100
    listSize = 10
    list = [randrange(intervalMinimun, intervalMaximum + 1) for _ in range(listSize)]

    for i in list:
        print(i, end = ' ')

    print()

    position = listSize - 1
    for i in reversed(range(0, len(list))):
        if list[i] <= 0:
            j = i
            while (j != position):
                j += 1
            if i != j and j - 1 >= 0: # if we actually moved in while loop and if the previous index is valid
                tmp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = tmp
                position = j - 1

    for i in list:
        print(i, end = ' ')


if __name__ == "__main__":
    main()
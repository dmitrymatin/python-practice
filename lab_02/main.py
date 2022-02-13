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
        item = list[i]

        j = i + 1

        while j <= listSize - 1 and list[j] > 0:
            list[j - 1] = list[j]
            j += 1
        
        list[j - 1] = item

    for i in list:
        print(i, end = ' ')


if __name__ == "__main__":
    main()
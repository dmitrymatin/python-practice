from random import randrange


def main():
    intervalMinimun = -100
    intervalMaximum = 100
    listSize = 10
    list = []
    for i in range(0, listSize):
        random_value = randrange(intervalMinimun, intervalMaximum + 1)
        list.append(random_value)

    for i in list:
        print(i, end = ' ')


if __name__ == "__main__":
    main()
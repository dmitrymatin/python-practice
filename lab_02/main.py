from random import randrange


def main():
    intervalMinimun = -100
    intervalMaximum = 100
    listSize = 10
    list = [randrange(intervalMinimun, intervalMaximum + 1) for _ in range(listSize)]

    for i in list:
        print(i, end = ' ')


if __name__ == "__main__":
    main()
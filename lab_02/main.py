from random import randrange


def main():
    intervalMinimun = -100
    intervalMaximum = 100
    listSize = 10
    list = [randrange(intervalMinimun, intervalMaximum + 1) for _ in range(listSize)]

    print('input sequence:')
    print(' '.join(str(item) for item in list))

    for i in reversed(range(0, len(list) - 1)):
        item = list[i]

        if item > 0:
            continue
        
        j = i + 1

        while j <= listSize - 1 and list[j] > 0:
            list[j - 1] = list[j]
            j += 1
        
        list[j - 1] = item

    print('output sequence:')
    print(' '.join(str(item) for item in list))


if __name__ == "__main__":
    main()
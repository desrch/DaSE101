if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    length = len(l)
    k = 0
    for i in range(length):
        j = length - 1 - i
        print(l[j])

    while k < length:
        m = length - 1 - k
        print(l[m])
        k += 1

    print(l[::-1])
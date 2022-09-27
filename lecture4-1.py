if __name__ == '__main__':
    res = 1
    for i in range(1,101):
        if i%2 == 1 :
            print(i)
            if i <= 50:
                res *= i

    print(res)
if __name__ == '__main__':
    string_a = input()
    length = len(string_a)
    cur = maxs = 1
    for i in range(length-1):
        if string_a[i] == string_a[i+1] :
            cur += 1
        else :
            if maxs < cur :
                maxs = cur
            cur = 1

    print(maxs)





if __name__ == '__main__':
    string_s = input()
    length = len(string_s)
    cnt = 0
    emp = []
    string_1 = ''
    string_res = ''
    for i in range(length):
        if string_s[i] == ' ':
            emp.append(i)
            cnt += 1

    for i in range(cnt):
        if i != cnt - 1:
            x = emp[i] + 1
            y = emp[i + 1] - 1
            string_1 = string_s[x:y + 1]
        else:
            string_1 = string_s[emp[i] + 1:]

        string_res += string_1
    if emp[0] != 0:
        string_res = string_s[0: emp[0]] + string_res

    print(string_res)

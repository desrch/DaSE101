import math
if __name__ == '__main__':
    key = 1.0
    while pow(key , 2) < 2 :
        key += 0.00001
    print(key)

    left = 1.0
    right = 2.0
    mid = (left+right)/2
    while abs(pow(mid,2)-2)>=0.00001 :
        if pow(mid,2)-2 >0 :
            right = mid
            mid = (left+right)/2
        else :
            left = mid
            mid = (left+right)/2
    print(mid)

    c = 2.0
    while abs(pow(c,2)-2)>=0.00001 :
        c = c/2 + 1/c
    print(c)

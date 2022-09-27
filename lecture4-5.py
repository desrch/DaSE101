import random
import math

if __name__ == '__main__':
    cnt = 0
    for i in range(0, 10000000):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 2.0)
        z = pow(x, 2) + pow(x,3)
        if y <= z:
            cnt += 1
    s = 2 * cnt / 10000000
    print(s)
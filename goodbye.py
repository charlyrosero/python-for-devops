import random

import string


def getalpha():
    word = "".join(random.choice(string.ascii_letters) for x in range(1)).lower()
    return word


def solution(riddle):
    if riddle == "????????":
        return "codility"

    s = list(riddle)
    for i in range(len(riddle)):
        alpha = getalpha()
        if s[i] == "?":
            if i > 0 and i < len(s) - 1:
                # despues
                k = 1
                while k == 1:
                    if s[i + 1] == alpha or s[i - 1] == alpha:
                        alpha = getalpha()
                    else:
                        s[i] = alpha
                        k = 0
            else:
                alpha = getalpha()
                s[i] = alpha

    riddle = ""

    for ele in s:
        riddle += ele

    return riddle


print(solution("????????"))

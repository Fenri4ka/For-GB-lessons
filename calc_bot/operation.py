import re


def math_op(some_str):
    s = some_str.split()
    while len(s) > 1:
        if ('/' in s or
                '*' in s):
            for i in range(len(s)):
                if s[i] == '/':
                    s[i] = float(s[i - 1]) / float(s[i + 1])
                    s.pop(i - 1)
                    s.pop(i)
                    break
                elif s[i] == '*':
                    s[i] = float(s[i - 1]) * float(s[i + 1])
                    s.pop(i - 1)
                    s.pop(i)
                    break
        else:
            for i in range(len(s)):
                if s[i] == '-':
                    s[i] = float(s[i - 1]) - float(s[i + 1])
                    s.pop(i - 1)
                    s.pop(i)
                    break
                elif s[i] == '+':
                    s[i] = float(s[i - 1]) + float(s[i + 1])
                    s.pop(i - 1)
                    s.pop(i)
                    break
    return s[0]


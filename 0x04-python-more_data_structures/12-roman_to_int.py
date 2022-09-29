#!/usr/bin/python3
def roman_to_int(roman_string):
    c = 0
    result = 0
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    s = list(roman_string)
    for b in range(len(s)):
        arr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(len(arr)):
            if (s[b] == arr[i]):
                s[b] = num[i]
                break
    if len(s) == 1:
        return (s[0])
    else:
        for d in range(1, len(s)):
            if s[d - 1] >= s[d]:
                result = result + s[d - 1]
            else:
                result = result - s[d - 1]
        result = result + s[d]
        return result

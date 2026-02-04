def swap_case(s):
    res = "" # strings are immutable so store in new space
    for char in s:
        if char.isupper():
            res += char.lower()
        else:
            res += char.upper()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
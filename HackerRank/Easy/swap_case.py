def swap_case(s):
    res = ""
    for i in range(len(s)):
        if s[i].isupper():
            res += s[i].lower()
        elif s[i].islower():
            res += s[i].upper()
        else:
            res += s[i]  
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

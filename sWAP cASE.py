def swap_case(s):
    result = ""
    for x in s:
        if x.isupper() == True:
            result+=(x.lower())
        else:
            result+=(x.upper())
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

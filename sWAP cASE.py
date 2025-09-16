def swap_case(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

if __name__ == '__main__':
    s = input()
    print(swap_case(s))


def to_lower(s):
    res = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            res += chr(ord(ch) + 32)
        else:
            res += ch
    return res

def to_upper(s):
    res = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        else:
            res += ch
    return res

def toggle_case(s):
    res = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            res += chr(ord(ch) + 32)
        else:
            res += ch
    return res


def remove_chars(one, remove):
    res = ""
    for ch in one:
        keep = True
        for r in remove:
            if ch == r:
                keep = False
                break
        if keep:
            res += ch
    return res

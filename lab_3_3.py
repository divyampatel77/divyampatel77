
def is_substring(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        match = True
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return True
    return False

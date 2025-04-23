def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sanitized list:", sanitize_list(lst))
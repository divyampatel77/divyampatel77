def average(lst):
    if not lst:
        return (0, 0)
    s, c = average(lst[1:])
    return (lst[0] + s, 1 + c)

lst = list(map(int, input("Enter numbers separated by space: ").split()))
s, c = average(lst)
print("Average:", s / c if c else 0)
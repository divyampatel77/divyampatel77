def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(lst))
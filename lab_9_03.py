def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in 'aeiou') + count_vowels(s[1:])

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
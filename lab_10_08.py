with open('sample_text.txt', 'r') as f:
    content = f.read()

words_to_remove = ['a', 'the', 'an']
for word in words_to_remove:
    content = content.replace(f' {word} ', ' ')

with open('cleaned_text.txt', 'w') as f:
    f.write(content)

print("Words removed and new file created.")
def find_occurrences(text, pattern):
    occurrences = []
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            occurrences.append(i)
    
    if not occurrences:
        return -1
    else:
        return occurrences

text = 'ABABDABACDABABCABAB'
pattern = 'ABABCABAB'

result = find_occurrences(text, pattern)
print(result)

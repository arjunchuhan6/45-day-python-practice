# 269. Write a regular expression
# Regular expressions (regex) for pattern matching

import re

print("=== Basic Pattern Matching ===")
pattern = r"python"  # Raw string
text = "I love python programming"

if re.search(pattern, text):
    print(f"Pattern '{pattern}' found in text")

print("\n=== Common Regex Patterns ===")
# . (dot) - matches any character except newline
print("Pattern: 'c.t' in 'cat', 'cut', 'cot':")
for word in ['cat', 'cut', 'cot', 'c9t']:
    if re.match(r'c.t', word):
        print(f"  Matched: {word}")

print("\n--- Character classes ---")
# [abc] - matches any character in the brackets
print("Pattern: '[aeiou]' in 'hello world':")
vowels = re.findall(r'[aeiou]', 'hello world')
print(f"  Vowels found: {vowels}")

print("\n--- Quantifiers ---")
# * (zero or more), + (one or more), ? (zero or one), {n} (exactly n)
pattern_list = [
    (r'ab*c', ['ac', 'abc', 'abbc', 'abbbc']),  # * - zero or more
    (r'ab+c', ['ac', 'abc', 'abbc', 'abbbc']),  # + - one or more
    (r'colou?r', ['color', 'colour', 'colr']),  # ? - zero or one
]

for pattern, words in pattern_list:
    print(f"\nPattern: '{pattern}'")
    for word in words:
        if re.match(pattern, word):
            print(f"  Matched: {word}")

print("\n=== Anchors ===")
# ^ (start), $ (end)
print("Pattern: '^hello' (starts with hello)")
for text in ['hello world', 'say hello', 'hello']:
    if re.match(r'^hello', text):
        print(f"  Matched: {text}")

print("\nPattern: 'world$' (ends with world)")
for text in ['hello world', 'world is beautiful', 'world']:
    if re.search(r'world$', text):
        print(f"  Matched: {text}")

print("\n=== Escaping Special Characters ===")
# Backslash escapes special characters
pattern = r'\d+'  # One or more digits
print(f"Pattern: '{pattern}' to find digits:")
digits = re.findall(pattern, 'Phone: 123-456-7890')
print(f"  Found: {digits}")

print("\n=== Common Character Classes ===")
print("\\d - digits:")
print(f"  {re.findall(r'\d', 'abc123def456')}")
print("\\w - word characters (letters, digits, underscore):")
print(f"  {re.findall(r'\w', 'hello_world-123!')}")
print("\\s - whitespace:")
print(f"  {re.findall(r'\s', 'hello   world')}")

import re
pattern = re.compile(r'\b(\w+)\b')
text = "Regex is a powerful tool for pattern matching."
matches = pattern.findall(text)
print(matches)
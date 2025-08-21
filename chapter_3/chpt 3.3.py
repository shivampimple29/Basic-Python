letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Donald").replace("<|Date|>", "19 Jan 2025"))
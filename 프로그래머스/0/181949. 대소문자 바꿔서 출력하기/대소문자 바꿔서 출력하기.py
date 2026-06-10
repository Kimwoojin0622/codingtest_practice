str = input()

result = []
for s in str:
    if s == s.lower():
        result.append(s.upper())
    else:
        result.append(s.lower())
        
print("".join(result))
def solution(my_string):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for s in my_string:
        if s not in vowels:
            result.append(s)
    
    return "".join(result)
def solution(my_string):
    F_alpha, E_alpha, f_alpha, e_alpha = ord('A'), ord('Z'), ord('a'), ord('z')
    result = [0] * (E_alpha - F_alpha + 1) + [0] * (e_alpha - f_alpha + 1)
    
    for s in my_string:
        word_to_asc = ord(s)
        if word_to_asc <= 90:
            result[word_to_asc - F_alpha] += 1
        if word_to_asc >= 97:
            result[word_to_asc - F_alpha - 6] += 1
        
    return result
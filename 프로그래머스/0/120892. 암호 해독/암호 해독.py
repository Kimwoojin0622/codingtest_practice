def solution(cipher, code):
    result = cipher[code-1::code]
    return result
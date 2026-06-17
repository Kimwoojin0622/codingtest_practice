def solution(myString):
    result = ['l' if ord(s) < ord('l') else s for s in myString]
    return "".join(result)
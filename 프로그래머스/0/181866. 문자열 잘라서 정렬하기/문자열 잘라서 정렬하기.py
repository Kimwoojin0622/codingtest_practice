def solution(myString):
    without_x = myString.split('x')
    result = [s for s in without_x if s != ""]
    result.sort()
    return result
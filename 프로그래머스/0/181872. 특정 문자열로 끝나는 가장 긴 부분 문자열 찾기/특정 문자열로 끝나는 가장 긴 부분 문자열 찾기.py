def solution(myString, pat):
    # rindex를 통해 myString에서 가장 오른쪽에 있는 pat을 찾는다.
    # ex) ABCdEcWdE면 -> 7이 출력된다
    #     012345678
    idx = myString.rindex(pat)
    result = myString[:idx + len(pat)]
    return result
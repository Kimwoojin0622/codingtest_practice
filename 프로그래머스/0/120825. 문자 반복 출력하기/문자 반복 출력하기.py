def solution(my_string, n):
    result = []
    for s in my_string:
        for _ in range(n):
            result.append(s)

    return "".join(result)
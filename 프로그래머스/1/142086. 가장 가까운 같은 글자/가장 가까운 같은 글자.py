def solution(s):
    tmp = {}
    result = []
    for i in range(len(s)):
        if s[i] not in tmp:
            tmp[s[i]] = i
            result.append(-1)
        else:
            result.append(i - tmp[s[i]])
            tmp[s[i]] = i

    return result
def solution(s):
    s, result = s[::-1], []
    
    for i in range(len(s)):
        cnt = 0
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                result.append(j - i)
                break
            else:
                cnt += 1
        if cnt == len(s) - i - 1:
            result.append(-1)
        
    return result[::-1]
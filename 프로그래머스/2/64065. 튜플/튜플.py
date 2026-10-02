def solution(s):
    # O(N)
    string_preprocessing = s.replace("{","")[:-1] + ','
    
    finish_preprocessing = []
    t = ''
    for sp in string_preprocessing:
        if sp == "}":
            t = t.replace(","," ").lstrip()
            tmp = t.split(" ")
            t = ''
            finish_preprocessing.append(tmp)
        else:
            t += sp
    
    finish_sorted = sorted(finish_preprocessing, key=lambda x:len(x))
    
    result = {}
    for data in finish_sorted:
        for i in range(len(data)):
            if data[i] not in result:
                result[data[i]] = 0
            result[data[i]] += 1
    
    answer = []
    for data in result.items():
        answer.append(int(data[0]))
    
    return answer
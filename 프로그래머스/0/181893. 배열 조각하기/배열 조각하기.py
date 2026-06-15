def solution(arr, query):
    result = arr.copy()
    for i in range(len(query)):
        if i % 2 == 0:
            result = result[:query[i] + 1]
            # print(result)
        elif i % 2 != 0:
            result = result[query[i]:]
            # print(result)
    
    return result

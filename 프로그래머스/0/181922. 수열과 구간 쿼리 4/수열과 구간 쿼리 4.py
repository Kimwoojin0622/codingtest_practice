def solution(arr, queries):
    for data in queries:
        s, e, k = data[0], data[1], data[2]
        print(s, e, k)
        # i는 0부터임!!
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
            # print(arr)
        
    return arr
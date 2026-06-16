def solution(rank, attendance):
    # [7, 2, 5, 4]인데 얘네의 rank에서의 인덱스가 [1, 2, 3, 4]임 그래서 a = 2, b = 4, c = 3임
    # [6, 5, 4] 인데 얘네의 rank에서의 인덱스가 [0, 2, 5] 임 그래서 a = 5, b = 2, c = 0임
    temp = {}
    for i in range(len(rank)):
        if attendance[i]:
            temp[rank[i]] = i

    temp_list = []
    result = sorted(temp)
    dict_result = temp.items()
    for data in result:
        for dict_data in dict_result: # O(N ^ 2)
            if data == dict_data[0]:
                temp_list.append(dict_data[1])

    answer = (temp_list[0] * 10000) + (temp_list[1] * 100) + temp_list[2]
    return answer

# enumerate 버전
# def solution(rank, attendance):
#     # [7, 2, 5, 4]인데 얘네의 rank에서의 인덱스가 [1, 2, 3, 4]임 그래서 a = 2, b = 4, c = 3임
#     # [6, 5, 4] 인데 얘네의 rank에서의 인덱스가 [0, 2, 5] 임 그래서 a = 5, b = 2, c = 0임
#     temp = []
#     for i, rnk in enumerate(rank):
#         if attendance[i]:
#             temp.append([rnk, i])
    
#     temp = sorted(temp)
#     result = (temp[0][1] * 10000) + (temp[1][1] * 100) + temp[2][1]
#     return result
    

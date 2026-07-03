def solution(numlist, n):
    diff_list = []
    i = 0
    for num in numlist:
        diff_list.append([num, abs(num - n)])
    # lambda를 활용해서 diff_list[1]번을 기준으로 오름차순을 한 뒤, diff_list[0]번을 기준으로 내림차순 진행
    sorted_diff = sorted(diff_list, key = lambda x : (x[1], -x[0]))
    result = [data[0] for data in sorted_diff]
    return result
    
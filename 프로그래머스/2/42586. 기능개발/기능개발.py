def solution(progresses, speeds):
    transaction_day = []
    # step 1. 남은 일수를 구하고, speeds를 통해 며칠동안 작업하는지 구한다(transaction_day).
    for i in range(len(progresses)):
        tmp = 100 - progresses[i]
        if tmp % speeds[i] == 0:
            transaction_day.append(tmp // speeds[i])
        else:
            transaction_day.append(tmp // speeds[i] + 1)
            
    # step 2. 며칠동안 작업하는지 구했으면, transaction_day를 돌면서 앞에 숫자보다 작은 애들을 포함시킨다.
    count, i, max_value = 0, 0, -1
    tmp_list = []
    while i < len(transaction_day):
        if transaction_day[i] > max_value:
            max_value = transaction_day[i]
            count += 1
        tmp_list.append(count)
        i += 1
        
    set_tmp, result = set(tmp_list), []
    
    for data in set_tmp:
        n = tmp_list.count(data)
        result.append(n)
    return result
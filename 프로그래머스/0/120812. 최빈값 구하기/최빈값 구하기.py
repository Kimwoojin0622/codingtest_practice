def solution(array):
    set_array = list(set(array)) # array의 중복 제거
    ele_cnt = []
    
    # array에서 중복을 제거한 set_array에서 for문을 사용해 각 원소를 꺼낸 뒤,
    # array에 각 원소가 몇개 있는지 count를 활용해 개수를 센 뒤, ele_cnt 리스트에 append
    for data in set_array:
        ele_cnt.append(array.count(data))
    
    # 각 원소의 count(개수)값을 담은 ele_cnt 배열에서, max 값이 여러 개면 return -1
    max_value = max(ele_cnt)
    if ele_cnt.count(max_value) > 1:
        return -1
    else:
        # 아니면, ele_cnt에서 개수 최대값이 있는 index를 찾은 뒤,
        # set_array[index]를 return한다.
        # 왜냐하면 set_arrary와 ele_cnt의 인덱스는 일치하기 때문이다.
        # 1이 5개, 3이 1개, 2가 8개라면
        # set_array[1, 3, 2] 이고, ele_cnt[5, 1, 8]이다.
        idx = ele_cnt.index(max_value)
        return set_array[idx]
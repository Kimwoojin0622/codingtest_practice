def solution(my_string, is_prefix):
    prefix_list = []
    # my_string에서 모든 접두사를 꺼내어 prefix_list에 append
    for i in range(len(my_string)):
        prefix_list.append(my_string[: i + 1])
        
    if is_prefix in prefix_list:
        return 1
    else:
        return 0
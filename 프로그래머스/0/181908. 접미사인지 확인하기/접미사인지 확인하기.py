def solution(my_string, is_suffix):
    is_suffix_list = [my_string[i:] for i in range(len(my_string))]
    
    if is_suffix in is_suffix_list:
        return 1
    else:
        return 0
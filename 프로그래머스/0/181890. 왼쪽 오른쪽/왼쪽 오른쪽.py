def solution(str_list):
    for s in str_list:
        idx = str_list.index(s)
        if s == 'l':
            return str_list[:idx]
        elif s == 'r':
            return str_list[idx + 1:]

    return []

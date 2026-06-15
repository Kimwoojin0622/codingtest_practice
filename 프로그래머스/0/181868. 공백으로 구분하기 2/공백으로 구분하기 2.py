def solution(my_string):
    chk = my_string.split(" ")
    result = []
    for data in chk:
        if data != "":
            result.append(data)
    return result
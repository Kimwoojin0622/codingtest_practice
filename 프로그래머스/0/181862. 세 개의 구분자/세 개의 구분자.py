def solution(myStr):
    temp = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').strip()
    answer = []
    if len(temp) >= 1:
        result = temp.split(" ")
        for data in result:
            if data != "":
                answer.append(data)
        return answer
    else:
        return ["EMPTY"]
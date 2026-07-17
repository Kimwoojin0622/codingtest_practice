def solution(s):
    ups, lows = [], [] # ups는 대문자 담을 리스트, lows는 소문자 담을 리스트
    for data in s:
        if data.lower() == data:
            lows.append(data)
        else:
            ups.append(data)
    
    lows.sort(reverse = True)
    ups.sort(reverse = True)
    
    return "".join(lows) + "".join(ups)
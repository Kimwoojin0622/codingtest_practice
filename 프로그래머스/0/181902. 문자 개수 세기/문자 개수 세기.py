def solution(my_string):
    # 문자를 아스키코드로 변환해서 대문자와 소문자 길이만큼 리스트를 만든다.
    F_value, L_value = ord('A'), ord('Z')
    f_value, l_value = ord('a'), ord('z')
    
    # 대문자 리스트
    # 대문자 A ~ Z 까지의 길이만큼 리스트 생성
    upper_list = [0] * (L_value - F_value + 1)
    # 만약 대문자 Z의 아스키코드 보다 작거나 같다면 A~Z이므로 그 값이 나오면 +1
    # +1 할 때도 A의 아스키코드는 65이고, 리스트의 시작값은 0이니, A의 아스키코드 값만큼 빼야한다.
    # ex ) [A, B, C] -> [65, 66, 67] -> A의 아스키코드 65만큼 빼면 -> [0, 1, 2] -> 리스트의 인덱스 값처럼 변환
    for s in my_string:
        if ord(s) <= L_value:
            upper_list[ord(s) - F_value] += 1
    
    # 소문자 리스트
    lower_list = [0] * (l_value - f_value + 1)
    for s in my_string:
        if ord(s) >= f_value:
            lower_list[ord(s) - f_value] += 1
    
    return upper_list + lower_list

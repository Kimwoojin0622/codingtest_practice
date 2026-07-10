def solution(common):
    chk= common[1:3]
    # chk[0] == 0일때 제외
    if chk[-1] == 0:
        tmp = chk[1] - chk[0]
        return common[-1] + tmp
    
    # 얌체 테스트케이스 등비수열 잡기
    if chk[0] % chk[1] == 0 and chk[1] == common[0]:
        return common[-1] * (chk[0] // chk[1])
    
    # 등차수열
    tmp = chk[0] - chk[1]
    if chk[0] + tmp == common[0]:
        tmp = chk[1] - chk[0]
        return common[-1] + tmp
    
    # 등비수열
    if chk[1] % chk[0] == 0:
        tmp = chk[1] // chk[0]
        return common[-1] * tmp
    
    return common
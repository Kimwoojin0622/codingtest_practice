def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_chk = [0, 0, 0, 0, 0, 0]
    
    for n in dice:
        dice_chk[n-1] += 1
    
    # step 3. 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 * p점을 얻는다
    # 각 주사위가 몇번 나왔는지 담아놓은 임시값 dice_chk
    if dice_chk.count(1) == 4:
        return min(dice)
    
    elif dice_chk.count(4) == 1:
        idx = dice_chk.index(4) + 1
        return 1111 * idx
    
    elif dice_chk.count(3) == 1:
        idx_p = dice_chk.index(3) + 1
        idx_q = dice_chk.index(1) + 1
        return (10 * idx_p + idx_q) ** 2
    
    elif dice_chk.count(2) == 2:
        dice_set = list(set(dice))
        p = dice_set[0]
        q = dice_set[1]
        return (p + q) * abs(p - q)
    
    else:
        temp = 1
        for i in range(len(dice_chk)):
            if dice_chk[i] == 1:
                temp = temp * (i + 1)
        return temp

    
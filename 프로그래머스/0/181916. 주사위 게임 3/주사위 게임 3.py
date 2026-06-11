def solution(a, b, c, d):
    # step 1. 주사위를 리스트에 담아준다.
    dice = [a, b, c, d]
    # step 2. 각 주사위가 몇번 나왔는지 확인할 수 있는 dice_chk 리스트를 생성한다.
    # ex ) [6, 2, 6, 3] 이면 6이 2번, 2가 1번, 3이 1번이다.
    # 이를 dice_chk에 집어넣게 되면 [0, 1, 1, 0, 0, 2]이 된다.
    dice_chk = [0, 0, 0, 0, 0, 0]
    for n in dice:
        dice_chk[n-1] += 1
    
    # step 3. 네 주사위에서 나온 숫자가 모두 다르면 a, b, c, d 중 최솟값을 return한다.
    # a, b, c, d 모두 값이 다르다면,
    # 각 주사위가 몇번 나왔는지 담아놓은 임시값 dice_chk에 1만 담기게 될 것이다.
    # 그러므로 dice_chk 리스트에 1을 count 했을 때 4면 주사위 값 중에 min()을 return한다.
    # ex) 1, 2, 3, 4 -> [1, 1, 1, 1, 0, 0] 이므로 count(1) == 4 이다.
    if dice_chk.count(1) == 4:
        return min(dice)
    
    # step 4. 네 주사위에서 나온 숫자가 모두 같다면 1111 * p를 return한다.
    # a, b, c, d 모두 값이 같다면 위와 동일한 방식으로 [0, 0, 0, 4, 0, 0] 일 것이다.
    # 그러므로 dice_chk 리스트에 4를 count 했을 때 1이면 1111 * (4의 인덱스값 + 1)을 return한다.
    # 왜냐하면 인덱스 값 + 1 이 주사위 값이기 때문이다.
    elif dice_chk.count(4) == 1:
        idx = dice_chk.index(4) + 1
        return 1111 * idx
    
    # step 5. 만약 네 주사위에서 나온 숫자가 3개가 같고, 하나가 다르다면 (10 * p + q)^2를 return한다.
    # 이도 위와 유사하게 [0, 0, 3, 0, 1, 0] 식으로 dice_chk가 만들어질 것이다.
    # 그럼 이제 index()를 써서, 각 주사위에 값을 알아낸 뒤, (10 * p + q)^2 의 값을 구하면 된다.
    elif dice_chk.count(3) == 1:
        idx_p = dice_chk.index(3) + 1
        idx_q = dice_chk.index(1) + 1
        return (10 * idx_p + idx_q) ** 2
    
    # step 6. 만약 네 주사위에서 나온 숫자가 2개씩 같다면, (p + q) * |p - q|를 return한다.
    # 이는 원래 a, b, c, d의 값을 담은 dice를 set을 하여 중복을 제거했다.
    # 중복을 제거하면 [4, 5, 4, 5] -> [4, 5] 결국엔 두 개만 남기 때문에 인덱스로 접근해서 풀었다.
    elif dice_chk.count(2) == 2:
        dice_set = list(set(dice))
        p = dice_set[0]
        q = dice_set[1]
        return (p + q) * abs(p - q)
    
    # step 7. 만약 네 주사위에서 나온 숫자가 2개가 같고, 나머지 두 개(q,r)가 서로 다르다면,
    # q * r을 return한다.
    # 이 부분은 [0, 0, 2, 1, 1, 0] 이러한 식으로 dice_chk가 만들어졌을 것이다.
    # 그러므로 리스트를 돌면서 만약 i값이 1과 같다면 temp에 i+1 값을 곱해주면서 결국 q * r의 형태로 만들었다.
    # i+1을 곱한 이유는 i는 0부터 시작하고 주사위는 1부터 시작하기 때문이다.
    else:
        temp = 1
        for i in range(len(dice_chk)):
            if dice_chk[i] == 1:
                temp = temp * (i + 1)
        return temp

    

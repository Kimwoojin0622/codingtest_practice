def divide_i(i, tmp, length):
    if i == (length - 1):
        return str(tmp)
    else:
        return str(tmp % 10)

def solution(a, b):
    # step 1. 더하기를 쉽게 하기 위해 a와 b를 거꾸로 만든다.
    # 왜냐하면 더하기는 앞에서부터 하는게 아닌, 뒤에서 부터 하기 때문이다.
    # 582 + 734를 생각해보면 맨 끝자리인 2 + 4를 먼저 수행한다.
    a, b = a[::-1], b[::-1]

    # step 2-1. a와 b중에 길이가 긴 것을 max()를 활용해 가져온다.
    # 왜냐하면 1234 + 56을 할 때, 1234 만큼 돌아야한다. 56의 길이만큼 도는 것이 아닌, 1234의 길이만큼 돌아야한다.
    length = max(len(a), len(b))
    
    # step 2-2. 더한 값을 저장할 수 있는 result 리스트를 생성하고,
    # 각 자리수를 더한 값을 저장하는 tmp와 몫을 저장하는 share 변수를 생성한다.
    # 만약 8 + 3이라고 하면, 8 + 3은 11이기 때문에, 11 // 10을 한 몫인 1을 남겨놔야한다. 왜냐하면 다음 자리수에 더해야되기 때문이다.
    # 그리고 11 % 10인 나머지 1을 result에 append() 한다.
    
    # 만약 9 + 5이라고 하면, 9 + 5는 14이고, 14 // 10인 1을 남겨두고, 4를 result에 append()를 하는 것이다.
    # 왜냐하면 14에서 4가 자리에 표시되기 때문이다.
    result = []
    tmp, share = 0, 0
    
    # step 3. step 2에서 설명한대로 코드를 작성했다.
    # a[i] + b[i] + 몫을 진행해서 그 자리의 값을 구한다.
    # 만약, a[2]번째인데, a[1] b[i]번째에서 9 + 5로 인해 14 // 10 = 1이 넘어왔다면 그 값까지 더해줘야되기 때문이다.
    for i in range(length):
        # step 4. 만약, i가 len(b)보다 더 길다면 b는 다 더한 상태이기 때문에, a와 몫만 더해준다.
        if i > len(b) - 1:
            tmp = int(a[i]) + 0 + share
            # step 5. 그리고, 만약 맨 앞자리 수가 두 자리수로 만들어진다면, 두 자리수를 return한다. divide_i 함수 생성
            # ex) 56 + 52를 해보면, 맨 앞 자리수가 5 + 5 = 10 두 자리이기 때문에 두 자리수를 return 해야됨.
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            share = tmp // 10
        # step 4. 만약, i가 len(a)보다 더 길다면 a는 다 더한 상태이기 때문에, b와 몫만 더해준다.
        elif i > len(a) - 1:
            tmp = 0 + int(b[i]) + share
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            share = tmp // 10
        else:
            tmp = int(a[i]) + int(b[i]) + share
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            share = tmp // 10
            
    
    # step 6. a와 b를 [::-1]를 활용해 뒤집어서 더했기 때문에, result도 [::-1]를 활용해 원래 상태로 만든다.
    result = result[::-1]
    return "".join(result)

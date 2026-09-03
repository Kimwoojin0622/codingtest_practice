def solution(keymap, targets):
    key_location = {}
    for key in keymap: # 100 * 100 이므로 O(N^2) 가능
        for k in key:
            if k not in key_location:
                key_location[k] = key.index(k) + 1
            elif k in key_location:
                if key.index(k) + 1 < key_location[k]:
                    key_location[k] = key.index(k) + 1
    
    result = [0] * len(targets)
    
    i = 0
    for target in targets: # 100 * 100
        target_sum = 0
        for t in target:
            if t not in key_location:
                target_sum = -1
                break
            else:
                target_sum += key_location[t]
        result[i] = target_sum
        i += 1

    return result
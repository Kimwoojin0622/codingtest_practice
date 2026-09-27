def solution(phone_book):
    phone_set = set(phone_book) # O(N)

    for phone in phone_set:
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    
    return True
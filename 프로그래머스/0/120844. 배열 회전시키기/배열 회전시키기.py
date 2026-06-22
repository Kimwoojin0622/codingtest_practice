from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    
    if direction == 'right':
        temp = queue.pop()
        queue.appendleft(temp)
        return list(queue)
    elif direction == 'left':
        temp = queue.popleft()
        queue.append(temp)
        return list(queue)

        
        
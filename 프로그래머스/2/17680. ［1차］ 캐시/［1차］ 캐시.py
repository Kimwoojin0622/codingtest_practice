from collections import deque
def solution(cacheSize, cities):
    # O(N^2) 불가
    cache = deque([])
    cities = [city.lower() for city in cities] # O(N) 100,000

    result = 0
    for city in cities: # O(N) 100,000
        if city not in cache and len(cache) < cacheSize: # O(M) 30
            cache.append(city)
            result += 5
        elif city not in cache and len(cache) >= cacheSize:
            cache.append(city)
            cache.popleft()
            result += 5
        elif city in cache:
            idx = cache.index(city)
            tmp = cache[idx]
            del cache[idx]
            cache.append(tmp)
            result += 1
    
    return result
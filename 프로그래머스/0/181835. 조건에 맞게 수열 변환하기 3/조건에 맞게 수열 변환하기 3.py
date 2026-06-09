def solution(arr, k):
    result = [n * k if k % 2 != 0 else n + k for n in arr]
    return result
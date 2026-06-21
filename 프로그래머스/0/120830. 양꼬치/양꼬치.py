def solution(n, k):
    drink_discount = (n // 10) * 2000
    return (n * 12000) + (k * 2000) - drink_discount
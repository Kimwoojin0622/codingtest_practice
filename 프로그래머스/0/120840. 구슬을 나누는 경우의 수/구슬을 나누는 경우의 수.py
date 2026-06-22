def factorial(num):
    temp = 1
    for i in range(num, 0, -1):
        temp = temp * i
    return temp
def solution(balls, share):
    # hint = n! / (n-m)! * m!
    n, m, nm = factorial(balls), factorial(share), factorial(balls - share)
    result = n / (nm * m)
    return result
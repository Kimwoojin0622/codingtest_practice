a, b = map(int, input().split(' '))

# b행 a열

stars = '*' * a
for _ in range(b):
    print(stars)
def maximum(*numbers):
    a = 0
    for i in numbers:
        if i > a:
            a = i
    return a
print(maximum(1, 22, 3, 2))

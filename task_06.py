def maximum(*numbers):
    a = numbers[0]
    for i in numbers:
        if i > a:
            a = i
    return a
print(maximum(-1, -22, 0, 5))

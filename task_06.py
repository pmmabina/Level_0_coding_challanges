def maximum(*numbers):
    max_num = numbers[0]
    
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
print(maximum(1, -22, 0, 5, 6))

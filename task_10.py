def common_charectors(first_string, second_string):
    for i in first_string:
        if i in second_string:
            print(i, end = ", ")
common_charectors("computers", "house")

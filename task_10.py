def common_charectors(first_string, second_string):
    com_letters = ""
    for i in second_string.lower():
        if i in com_letters:
            pass
        elif i in first_string.lower():
            com_letters += i
    print("Common letters: " + ", ".join(com_letters))   
common_charectors('house','computers')

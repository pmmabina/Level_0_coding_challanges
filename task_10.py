def common_charectors(first_string, second_string):
    com_letters = ""
    for letters in second_string.lower():
        if letters in com_letters:
            pass
        elif letters in first_string.lower():
            com_letters += letters
    print("Common letters: " + ", ".join(com_letters))   
common_charectors('house','computers')

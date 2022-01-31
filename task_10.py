def common_charectors():
    first_string = input("Enter the first string ")
    second_string = input("Enter the second string ")
    
    for i in first_string:
        if i in second_string:
            print(i, end = ", ")
            
common_charectors()

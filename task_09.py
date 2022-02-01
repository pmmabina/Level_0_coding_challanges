def check_vowels(string):
    vowels = ["a", "e", "i" ,"o" ,"u","A", "E", "I", "O", "U"]
    for i in string:
        if i in vowels:
            print(i, end=" ")      
check_vowels("Umuzi")

def check_vowels(string):
    vowels = ["a", "e", "i" ,"o" ,"u","A", "E", "I", "O", "U"]
    list = ""
    for letters in string.lower():
        if letters in list:
            pass
        elif letters in vowels:
            list += letters
    print("Vowels: " + ', '.join(list))
check_vowels("UMUZI")

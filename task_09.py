def check_vowels(string):
    vowels = ["a", "e", "i" ,"o" ,"u","A", "E", "I", "O", "U"]
    found_vowels = ""
    for letters in string.lower():
        if letters in found_vowels:
            pass
        elif letters in vowels:
            found_vowels += letters
    print("Vowels: " + ', '.join(found_vowels))
check_vowels("Umuzi")

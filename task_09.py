def check_vowels(string):
    vowels = ["a", "e", "i" ,"o" ,"u","A", "E", "I", "O", "U"]
    list = ""
    for i in string.lower():
        if i in list:
            pass
        elif i in vowels:
            list += i
    print("Vowels: " + ', '.join(list))
check_vowels("Umuzi")

def check_vowels(string):
    vowels = ["a", "e", "i" ,"o" ,"u","A", "E", "I", "O", "U"]
    list = ""
    for i in string:
        if i in list.lower():
            pass
        elif i in vowels:
            list += i
    print("Vowels: " + ', '.join(list))
check_vowels("Umuzi")

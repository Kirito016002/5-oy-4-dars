################################################################################################### Masala1

def check_elements(text_1:str, text_2:str)->bool:
    result = True
    data = text_1.split()
    for i in range(len(data)):
        if data[i] not in text_2:
            result = False
            break
    return result

# print(check_elements("olma gilos", "olma anor banan uzum gilos"))

################################################################################################### Masala2

def check_vowel(data:str)->int:
    vowel = set()
    num = 0
    for i in data:
        if i in ["a", "o", "i", "e", "u"]:
            vowel.add(i)
            num += 1
    return num, vowel

# print(check_vowel("Gilos"))

################################################################################################### Masala3

def check_zero(*args)->int:
    num = 0
    for i in args:
        if i == 0:
            num += 1
    return num

# print(check_zero(1,3,0,5,0,4,5,0,6,0,8))

################################################################################################### Masala4

def check_allvowel(text_1:str, text_2:str)->bool:
    result = True
    vowels = check_vowel(text_1)[1]
    allvowels = check_vowel(text_2)[1]
    for i in vowels:
        if i not in allvowels:
            result = False
            break
    return result
# print(check_allvowel("a", "Olma gilos"))

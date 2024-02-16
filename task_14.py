string = "Celebration"

def find_vowels(str):
    result = 0
    vowels = "aouie"
    for alp in str:
        if alp in vowels:
            result += 1
    print(result)


find_vowels(str=string)
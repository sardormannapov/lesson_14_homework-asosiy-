def repl_vowels(str, simbol):
    result = ""
    vowels = "aouie"
    for alp in str:
        if alp in vowels:
            result += simbol

        else:
            result += alp

    print(result)

print(repl_vowels("the aardvark", "#"))

inp = input("Enter mood: ")

def default_mood(input):
    if input:
        print(f"Today i'm feeling {input}")

    else:
        print("Today i'm feeling natural")


default_mood(input=inp)
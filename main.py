from constants import MORSE_CODE_DICT, logo 

def translate(s):
    translated = [MORSE_CODE_DICT.get(l, "<missing code>") for l in s.upper()]
    return translated

def run_translator():
    input_word = input("What word do you wish to convert to Morse Code?\n> ")
    translated_word = translate(input_word)
    print(f"In Morse Code, `{input_word}` is:\n {" ".join(translated_word)}")
    go_again = input("Do you want to convert another word? y or n\n> ")
    if go_again == "y":
        run_translator()

if __name__ == "__main__":
    print(logo)
    run_translator()

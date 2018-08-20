from googletrans import Translator
import sys
import argparse

def translate(input_text):
    translator = Translator()
    translated_word = translator.translate(input_text)
    return translated_word.text

def setup():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--text", required=True, help="Add the input text")
    return parser.parse_args()

def main():
    args = setup()
    input_text = args.text
    print(translate(input_text))

if __name__ == "__main__":
    sys.exit(main())
    

def make_sentence(word: str, part_of_speech: int):
  
   #   Prints a sentence with the provided word based on the part of speech.

    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0 for noun, 1 for verb, or 2 for adjective.")


def main():
    word = input("Please type a noun, verb, or adjective: ")  # Get the word from the user
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))  # Get part of speech
    make_sentence(word, part_of_speech)  # Call the function to make the sentence


if __name__ == '__main__':
    main()

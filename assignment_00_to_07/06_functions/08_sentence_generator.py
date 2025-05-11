# Function to create a sentence based on the part of speech
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:  # If it's a noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:  # If it's a verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:  # If it's an adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:  # If invalid input is given
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

# Main function
def main():
    word = input("\033[34mPlease type a noun, verb, or adjective: \033[0m")  # Ask user for a word
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("\033[34mType 0 for noun, 1 for verb, 2 for adjective: \033[0m"))  # Ask for the part of speech
    make_sentence(word, part_of_speech)  # Call function to create and print sentence

# Run main if this file is executed
if __name__ == '__main__':
    main()

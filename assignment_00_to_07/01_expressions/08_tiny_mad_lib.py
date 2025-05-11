SENTENCE_START: str = "Learning programming is awesome. I used Python to create my "  # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Type an adjective and press enter: ")
    noun: str = input("Type a noun and press enter: ")
    verb: str = input("Type a verb and press enter: ")

    # Concatenate the sentence starter with the user's inputs to form a complete sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Call the main function
if __name__ == '__main__':
    main()
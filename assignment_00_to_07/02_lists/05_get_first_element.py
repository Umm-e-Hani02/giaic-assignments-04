# This program asks for a list and shows the first item

def get_first_element(list):
    # Shows the first item in the list
    print(list[0])

def get_list():
    # Makes a list by asking the user to type items
    # User can press Enter to finish adding items
    list = []
    element: str = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    # Runs the program
    # Gets a list and shows its first item
    list = get_list()
    get_first_element(list)

if __name__ == '__main__':
    main()
def get_last_element(list):
    print(f"The Last element in the list is: {list[-1]}")

def main():

    x = int(input("Enter the number of elements in the list: "))
    list = []

    for i in range(x):
        element = input(f"Enter element {i+1}: ")
        list.append(element)

    get_last_element(element)

if __name__ == '__main__':
    main()
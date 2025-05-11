def greet(name):
    # return Hello + name
    return "Hello " + name + "!"

def main():
    # Taking name as input
    name = input("\033[1;3mWhat's your name? \033[0m")
    print(greet(name))


if __name__ == "__main__":
    main()


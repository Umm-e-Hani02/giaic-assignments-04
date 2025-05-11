# Simple Mad Libs Game

print("Welcome to Mini Mad Libs!")

name = input("Enter a name: ")
place = input("Enter a place: ")
thing = input("Enter a thing: ")

story = f"""\nOnce upon a time, {name} went to {place}. There they found a mysterious {thing}. And that's how the adventure began!"""

print(story)

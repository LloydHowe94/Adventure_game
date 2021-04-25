# udacityprojectadventuregame
# DevonHowe

# Global imports
import time
import random

# functions


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {monster} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("You find yourself in an open field.")
    print_pause("There is a cave to your right and a house to your left.")
    print_pause("Enter 1 to peer into the cave")
    print_pause("Enter 2 to knock on the house door")
    print_pause("What would you like to do?")
    user_choice = check_input()
    if user_choice == '1':
        cave(monster)
    else:
        house(False, monster)


def cave(monster):
    print_pause("You found a sword behind a rock.")
    print_pause("You throw away your dagger.")
    print_pause("You are back in the field.")
    print_pause("Enter 1 to peer into the cave")
    print_pause("Enter 2 to knock on the house")
    print_pause("What would you like to do?")
    user_choice = check_input()
    if user_choice == '1':
        cave(monster)
    else:
        house(True, monster)


def house(sword, monster):
    print_pause("You knock on the door of the house.")
    print_pause(f"The {monster} comes out.")

    if sword is True:
        print_pause("He notices your sword and runs away.")
        print_pause("You win")

    else:
        print_pause("He engages you in combat.")
        print_pause("Enter 1 to fight")
        print_pause("Enter 2 to run away")
        print_pause("What would you like to do?")
        user_choice = check_input()

        if user_choice == '1':
            print_pause(f"You lose the game the {monster} caught you slippin "
                        "you got murked")

        else:
            print_pause("You are back in the field.")
            print_pause("Enter 1 to peer into the cave")
            print_pause("Enter 2 to knock on the house")
            print_pause("What would you like to do?")
            user_choice = check_input()
            if user_choice == '1':
                cave(monster)
            else:
                house(False, monster)


def check_input():

    #  check to see if the user can first enter correct input
    user_choice = input("Please enter a 1 or a 2: ")
    if (user_choice == '1' or user_choice == '2'):
        #  if the user enters correctly
        #  return the user choice and dont continue with function
        return user_choice
        #  if the user doesnt enter correctly keep asking
        #  for input until they enter the correct option
    while (True):
        print("Invalid input")
        user_choice = input("Please enter a 1 or a 2: ")
        if (user_choice == '2' or user_choice == '1'):
            break
    return user_choice


if __name__ == '__main__':
    monsters = ['pirate', 'ogre', 'ghosts', 'aliens', 'bigfoot']
    random_monster = random.choice(monsters)
    intro(random_monster)
    print_pause("Would you like to play again.")
    print_pause("Enter 1 for yes Enter 2 for no.")
    user_choice_valid = check_input()

    while (user_choice_valid == '1'):
        intro(random_monster)
        print_pause("Would you like to play again.")
        print_pause("Enter 1 for yes Enter 2 for no.")
        user_choice_valid = check_input()

    print_pause("GoodBye!")

import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Malcolm Cusack                        |
# Last Modified: 10/27/19, 2019         |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# A class to define what a pokemon is

class Pokemon:

    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.types = types

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_combat_points(self):
        return self.combat_points

    def get_types(self):
        return self.types

# -----------------------------------

# This function prints out a list of all the pokemon

def print_pokedex(pokedex):
    for pokemon in pokedex:
        answer = ""
        answer += "Number: " + str(Pokemon.get_number(pokemon)) + ", "
        answer += "Name: " + Pokemon.get_name(pokemon) + ", "
        answer += "CP: " + str(Pokemon.get_combat_points(pokemon)) + ": "
        answer += "Type: "
        answer += " and ".join(Pokemon.get_types(pokemon))
        print(answer)

# ------------------------------------

# This function lets user look up pokemon from by name

def lookup_by_name(pokedex, name):
    flag = 0
    for pokemon in pokedex:
        answer = ""
        if Pokemon.get_name(pokemon) == name:
            answer += "Number: " + str(Pokemon.get_number(pokemon)) + ", "
            answer += "Name: " + Pokemon.get_name(pokemon) + ", "
            answer += "CP: " + str(Pokemon.get_combat_points(pokemon)) + ": "
            answer += "Type: "
            answer += " and ".join(Pokemon.get_types(pokemon))
            print(answer)
            flag = 1
            
    if flag == 0:
        print("There is no Pokemon named " + str(name))

# -------------------------------------

# This function lets user look up pokemon from by number

def lookup_by_number(pokedex, number):
    flag = 0
    for pokemon in pokedex:
        answer = ""
        if Pokemon.get_number(pokemon) == number:
            answer += "Number: " + str(Pokemon.get_number(pokemon)) + ", "
            answer += "Name: " + Pokemon.get_name(pokemon) + ", "
            answer += "CP: " + str(Pokemon.get_combat_points(pokemon)) + ": "
            answer += "Type: "
            answer += " and ".join(Pokemon.get_types(pokemon))
            print(answer)
            flag = 1
            
    if flag == 0:  
        print("There is no Pokemon number " + str(number))

# --------------------------------------

# This function adds up all the different types of a pokemon from user input

def total_by_type(pokedex, pokemon_type):

    count = 0
    for pokemon in pokedex:
        for i in Pokemon.get_types(pokemon):
            if i == pokemon_type:
                count += 1
    print("Number of Pokemon that contain type: " + pokemon_type + " = " + str(count))
            
# --------------------------------------

# This function adds up total combat points from every pokemon

def average_hit_points(pokedex):
    summ = 0.0
    count = 0.0
    average = 0.0
    for pokemon in pokedex:
        summ += Pokemon.get_combat_points(pokemon)
        count += 1

    average = summ / count
    print("Average Pokemon combat points = {:.2f}".format(average))
        

# --------------------------------------

# Prints menu that user can use to choose other functions to use

def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokedex by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points.")
    print("6. Quit")
    print()

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()

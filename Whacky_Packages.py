import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Malcolm Cusack         
# Last Modified: 11/20/2019               
# ---------------------------------------------
""" This Program takes a file of Whaky Package cards and puts them into an array,
than campares these cards to the a file containing cards that you kown.
using the array made from before. There are also methods that compute you collection's
value as well as identifing how many missing cards there are and how much it
would cost you to buy the missing cards"""
# ---------------------------------------------

""" This class is used to set up a object of all the Wacky package cards"""

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)

# The STR method used to print the output of the cards

    def __str__(self):
        answer = ("My " + str(self.year) + " collection of " + self.manufacturer + " Wacky Packages\n\n")
        answer += ("Number    Description                  Value     Owned\n")
        answer += ("------    -----------                  -----     -----\n")
        for card in self.cards:
            answer += str(card) + "\n"
        return answer

# This method reads all the cards from a file then loops through and puts the
# cards into a numpy array call self.cards.

    def read_series_information(self, file_name):
        all_cards = open(file_name, "r")
        count = 0

        for line in all_cards:
            data = line.split(",")
            card = WackyPackageCard(int(data[0]), data[1], int(data[2]))
            self.cards[count] = card
            count += 1
            
        all_cards.close()

# This method reads a file containing the cards owned by you, then updates a
# card method set_cards_owned by comparing the array of self.cards to the file
# of the cards you own.

    def read_collection_information(self, file_name):
        my_cards = open(file_name, "r")
        
        for line in my_cards:
            for card in self.cards:
                cd = card.get_description()
                cards_owned = card.get_cards_owned()
                if line.strip().lower() == cd.strip().lower():
                    card.set_cards_owned(cards_owned + 1)

        my_cards.close()

# This method determines the value of cards owned by looping through the self.cards
# array and muliplying the cards owned by cards value and adding it to the total.

    def collection_value(self):
        total = 0
        
        for card in self.cards:
            total = total + (card.get_cards_owned() * card.get_value())
        return total

# This method determines missing information by looping through the all cards
# array and each time it sees that a card owned is 0 it adds to count and
# adds that cards value to total then returns both

    def determine_missing_information(self):
        count = 0
        total = 0
        
        for card in self.cards:
            if card.get_cards_owned() == 0:
                count += 1
                total += card.get_value()

        return [count , total]
                      
# ---------------------------------------------

""" This class is used to make a single card. That then gets put into
the Series of cards array called self.cards."""

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number

# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    print("Number of missing cards =", number_of_missing_cards)
    print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()

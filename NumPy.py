# -------------------------------
# CSCI 127, Program 3           |
# October 16, 2019              |
# Malcolm Cusack & Mathew Hamam |
# -------------------------------

def rating_average(file_name):

#This function as a user for a publisher, then it sorts through the data
#to average the rating of all the games, publisher rating, total sales and
#Publisher slaes. Then compares publisher states to tottal stats.

    """ All the variables """
   
    file = open(file_name, "r")
    line = file.readline()
    flag = input("Enter A Publisher you would like to know the average game rating of and total sales from 2004 to 2008: ")
    publisher_sum = 0
    total_sum = 0
    publisher_sales = 0.0
    total_sales = 0.0
    count = 0
    count2 = 0

    """Below scans through the file averaging and totalling the data"""
   
    for line in file:
        data = line.split(",")
        total_sum = total_sum + int(data[-27][1:-1])
        total_sales = total_sales + float(data[-26][1:-1])
        count2 += 1
        if str(data[-29][1:-1]).lower() == str(flag).lower():
            publisher_sum = publisher_sum + int(data[-27][1:-1])
            publisher_sales = publisher_sales + float(data[-26][1:-1])
            count += 1

    """ The math """

    total_sales = total_sales * 1000000
    publisher_sales = publisher_sales * 1000000
    rating_average = publisher_sum / count
    total_average = total_sum / count2

    """ The formating and printing """

    print("\n{:s}'s Total Sales Compared to {:s}'s Average Rating: \n".format(flag, flag))
    print("Average Rating: {:.2f} Out Of 100.".format(rating_average))
    print("Total Sales: ${:,.2f}".format(publisher_sales))
    print("--------------------------------------------------------------")
    print("Total Average: {:.2f} Out Of 100.".format(total_average))
    print("Total Sales: ${:,.2f}".format(total_sales))
    print("--------------------------------------------------------------\n")

# -------------------------------
 
def func1(file_name):
    #Takes publisher, genre, and lower and upper year bounds as user inputs,
    #and prints a list of all games within provided parameters with their
    #corresponding review score, sorted by review score in descending order
    file = open(file_name, "r")
    list_games = []
    list_scores = []
    publisher = str(input("Enter a publisher: "))
    genre = str(input("Enter a genre: "))
    year_lower = int(input("Enter a lower year bound between 2004 and 2010: "))
    year_upper = int(input("Enter an upper year bound below 2010: "))
    file.readline()
    for line in file:
        #iterates every line in csv file, using if conditionals to check if
        #that list entry meets the user provided requirements
        data = line.split(",")
        if str(data[-29][1:-1]) == publisher:
            genres = str(data[5][1:-1])
            genres = genres.replace('/', ' ')
            genre_list = genres.split()
            if genre in genre_list:
                if year_lower <= int(data[-21][1:-1]) <= year_upper:
                    #if a game meets the requirements, the title is added to
                    #a list of games, and its score is added to a list of scores
                    list_games.append(str(data[0]))
                    list_scores.append(int(data[-27][1:-1]))
    combined_list = []
    for x in range(len(list_games)):
        #combines names and scores into a single list composed of all sublists,
        #each containing the name as the first entry and its score as the second
        item = [list_games[x], list_scores[x]]
        combined_list.append(item)
    combined_list = sorted(combined_list, key = lambda game: game[1], reverse = True)
        #sorts the combined list in descending order of scores
    print("\nList of " + publisher + " " + genre + " games from "
          + str(year_lower) + " to " + str(year_upper) + ", sorted by review scores.")
    print("--------------------------------------------------------------")
    for i, item in enumerate(combined_list, 1):
        #prints numbered list of games and scores
        print(str(i).rjust(3) + '. ' + item[0] + ', ' + str(item[1]))
    print("\n")

# --------------------------------

def func2(file_name):
        #Takes a publisher as user input, and calculates the average completion time,
        #as well as average completionist time, average main and extras completion
        #time, and story completion time for all their games
        file = open(file_name, "r")
        list_avg = []
        list_comp = []
        list_mainplus = []
        list_story = []
        publisher = str(input("Enter a publisher: "))
        file.readline
        for line in file:
            #iterates through every line in csv file, and adds completion times to
            #four separate lists for each type of completion for every games fitting
            #the publisher requirement
            data = line.split(",")
            if str(data[-29][1:-1]) == publisher:
                list_avg.append(float(data[-20][1:-1]))
                list_comp.append(float(data[-15][1:-1]))
                list_mainplus.append(float(data[-10][1:-1]))
                list_story.append(float(data[-5][1:-1]))
        #Now the average is calculated for every list and rounded to 2 decimal points
        avg_avg = round((sum(list_avg))/(len(list_avg)), 1)
        comp_avg = round((sum(list_comp))/(len(list_comp)), 1)
        mainplus_avg = round((sum(list_mainplus))/(len(list_mainplus)), 1)
        story_avg = round((sum(list_story))/(len(list_story)), 1)
        print("\nThe average time to complete any game made by " + publisher +
            " is " + str(avg_avg) + " hours, with " + str(comp_avg) + " hours being"
            " the average time to complete everything, " + str(mainplus_avg) + " hours"
            " to complete the main game and the major extras, and " + str(story_avg)
            + " hours to complete just the story.")

# ------------------------------
       
def main(file_name):
    rating_average(file_name)
    func1(file_name)
    func2(file_name)

# ------------------------------
   
main("video_games.csv")

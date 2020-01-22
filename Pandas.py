import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 6: Pandas with Video Game File
# Malcolm Cusack
# Last Modified: 12/4/2019
# ---------------------------------------------

# Left commmented out code in my program so I could refer back to it.
# I experimented a lot with this program.


"""
Each function creates it's own graph, the first is designed to show how many
games were made each year tottal. I did this by making 2 arrays, one to old
how many games were made each year. The other to hold each year for labeling.
I looped through each year and if the year was equal to the year needed it'd
add to that index of the array. I leared saw that there were many more games
made in 2007 & 2008 than 2004 - 06. Makes sense. Another insight was that
there was over 400 games made in 2007. This must have been when video games
hit a tipping point in popularity.
"""


def games_made_in_year(data):
    year_count = np.zeros(5)
    years = np.array([2004, 2005, 2006, 2007, 2008])

    for index, row in data.iterrows():
        # print(row['Release.Year'])
        if row['Release.Year'] == 2004:
            year_count[0] += 1
        elif row['Release.Year'] == 2005:
            year_count[1] += 1
        elif row['Release.Year'] == 2006:
            year_count[2] += 1
        elif row['Release.Year'] == 2007:
            year_count[3] += 1
        elif row['Release.Year'] == 2008:
            year_count[4] += 1

    #plt.plot(years, year_count, "black", linewidth = 3)
    plt.bar(years, year_count,  color="g")
    plt.xlabel("Year")
    plt.ylabel("Games Made")
    plt.title("How many games made per year")
    plt.show()


"""
This function is designed to create a pie chart showing the metric sales of
each Call of Duty game and saving them into a new data frame. I did this by searching the DF for all titles with
the name Call of Duty in it. Then dropped all duplicated because there were many
duplicates. I reset the data frame once fixed. I put all the names of each COD
in an array so I could set my labels. There is an error message that doesn't effect
anything. I couldn't figure out how to fix it without adding all the duplicates
back in. I learned that COD 4 was by far the most popular COD. This is known to
be one of the best so the DF proved it. Also that COD 4 and COD World at War make
up more than half of the tottal sales. Shows how popular COD got with those 2
video games. It would be interesing to see Mondern Warfare 2s metric sales
compared to these.
"""


def cod_average_rating(data):
    cod_df = (data.loc[data['Title'].str.contains('Call of Duty')])
    cod_df.drop_duplicates(subset='Title', keep='first', inplace=True)
    cod_df.reset_index(drop=True, inplace=True)
    labels = cod_df['Title'].to_numpy(dtype=str)
    cod_df.plot.pie(y='Metrics.Sales', labels=labels, figsize=(10, 7))
    plt.title("Metric Sales of each Call of Duty game made.")
    plt.legend(loc="center")
    plt.show()


def main(file_name):

    data = pd.read_csv(file_name)
    # print(data['Title'])
    # print(data.head(1))
    # print(data.iloc[0,0])
    # print(data.loc[(data['Metadata.Publishers'] == 'EA') & (data['Metadata.Genres'] == 'Sports')] & (data['Title'])
    games_made_in_year(data)
    cod_average_rating(data)


main("video_games.csv")

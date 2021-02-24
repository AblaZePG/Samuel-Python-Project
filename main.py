#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Samuel Joses Daniel
#Group Name: Python Makkalz
#Class: <PN2004J>
#Date: <16 Feb 2020>
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pie chart
import matplotlib.pyplot as pit


#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
	def __init__(self):

		#load excel data (CSV format) to dataframe - 'df'
		dataframe = pd.read_csv('MonthyVisitors.csv')
		#show specific country dataframe
		sortCountry(dataframe)


#########################################################################
#CLASS Branch: End of Code
#########################################################################


#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    print(df)

    #display a specific country (Japan, Hong Kong, China, Taiwan, Republic of Korea) in column #9,10,11,12 and 13

    country_label1 = df.columns[9]
    print("\n" + country_label1 + "was selected.")
    country_label2 = df.columns[10]
    print("\n" + country_label2 + "was selected.")
    country_label3 = df.columns[11]
    print("\n" + country_label3 + "was selected.")
    country_label4 = df.columns[12]
    print("\n" + country_label4 + "was selected.")
    country_label5 = df.columns[13]
    print("\n" + country_label5 + "was selected.")

    #reading columns
    df.columns

    #sorting dataframe (rows and columns)
    print("\nThe following dataframe are read as follows: \n")
    SortedDF = (df[[
        'Year', 'Month', ' Japan ', ' Hong Kong ', ' China ', ' Taiwan ',
        ' Korea, Republic Of '
    ]][242:373])
    #Printing The data
    print(SortedDF)

    # This will convert dtypes from object to int
    SortedDF[' Japan '] = SortedDF[' Japan '].astype(int)
    SortedDF[' Hong Kong '] = SortedDF[' Hong Kong '].astype(int)
    SortedDF[' China '] = SortedDF[' China '].astype(int)
    SortedDF[' Taiwan '] = SortedDF[' Taiwan '].astype(int)
    SortedDF[' Korea, Republic Of '] = SortedDF[' Korea, Republic Of '].astype(
        int)

    #Removing unwanted Columns
    New = SortedDF.drop(['Year', 'Month'], axis=1)
    
    #Add up the total amount of visitors
    total = New.sum()

    #Sorting on descending order
    Sortedvalue = total.sort_values(ascending=False)

    #Reverting back from Integers to Objects
    Sortedvalue = Sortedvalue.reset_index()
    
    #Adding in column labels
    Sortedvalue.columns = ['Countries', 'Visitors']
    

    #Sorting toward top 3 countries
    print(
        "The Top 3 countries of visitors to Singapore from the span of 10 years are: "
    )
    print(Sortedvalue.head(n=3))
    #pie chart
    activities = ['China', 'Japan', 'Korea, Republic Of']
    slices = [7941631, 7443381, 3797093]
    colours = ['r', 'g', 'm']

    pit.pie(slices,
            labels=activities,
            startangle=90,
            shadow=True,
            explode=(0.2, 0, 0),
            autopct='%1.2f%%')

    pit.legend(loc="upper left")

    pit.show()

    return


#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':

	#Project Title
	print('######################################')
	print('# Data Analysis App - PYTHON Project #')
	print('######################################')

	#perform data analysis on specific excel (CSV) file
	  

#########################################################################
#Main Branch: End of Code
#########################################################################

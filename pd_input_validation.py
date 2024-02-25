'''

Data Input and Validation
Benjamin Teixeira
    
Filename: pd_input_analysis
    
Description: Data Input & Validation and
             Analysis in Python Pandas
    
'''
# running libraries and datasets: skiprows
import pandas as pd
olympics = pd.read_csv('olympics.csv',skiprows=1)

# Data Input and Validation -------------------------------------------

# Shape: Rows, Columns, and Both
print(olympics.shape) # Both
print(olympics.shape[0]) # Rows
print(olympics.shape[1]) # Columns

# first and last 5 rows of data
print(olympics.head())
print(olympics.tail())

# first 8 rows of data
print(olympics.head(8))

# information on dataframe
print(olympics.info())

# Basic Analysis ----------------------------------------------------

# Using value_counts to find medal counts
# per series within the dataframe
cities = olympics.City.value_counts()
print(cities)
sports = olympics.Sport.value_counts(dropna=True)
print(sports)

# Using sort_values along either axis
sorted_cities = olympics.City.sort_values()
print(sorted_cities)
ath_ed = olympics.sort_values(by=['Edition','Athlete'])
print(ath_ed)

# Boolean Indexing

# Identifying athletes by medal type
gold = olympics[olympics.Medal == 'Gold']
silver = olympics[olympics.Medal == 'Silver']
bronze = olympics[olympics.Medal == 'Bronze']

# Using boolean indexing for multiple conditions: women's gold
gold_women = olympics[(olympics.Medal == 'Gold') & (olympics.Gender == 'Women')
                      & (olympics.Event_gender == 'W')]
print(gold_women)

# Using boolean indexing for multiple conditions: swimming or men
swimming_or_men = olympics[(olympics.Discipline == 'Swimming')
                              | (olympics.Gender == 'Men')
                              | (olympics.Event_gender =='M')]
print(swimming_or_men)

# String Handling: Pulling information on fastest women's runner & MJ
flo_jo = olympics[olympics.Athlete.str.contains('Florence')]
print(flo_jo)
kobe = olympics[olympics.Athlete.str.contains('Kobe')]
print(kobe)

# Basic Analysis Questions --------------------------------------------
# jesse owens stats
jesse = olympics[olympics.Athlete == 'OWENS, Jesse']
print(jesse)

# badminton gold medals by country
badminton = olympics[(olympics.Discipline == 'Badminton') &
                      (olympics.Event == 'singles') &
                      (olympics.Medal == 'Gold')]
sorted_badminton = badminton.sort_values(by=['NOC','Athlete'])
sorted_noc_bad = badminton.NOC.sort_values()
print(sorted_badminton)
print(sorted_noc_bad)

# countries with most medals from 1984 to 2008
years = olympics[olympics.Edition >= 1984] 
years_medals = years.NOC.value_counts()
print(years_medals.head(3))


































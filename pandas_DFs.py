'''

LinkedIn Learning
Benjamin Teixeira
    
Filename: pandas_essentials
    
Description: essential training in Pandas: Series and DataFrames
    
'''

# running libraries
import pandas as pd

# testing basic arithmetic equations
32*32

# pandas installed versions and all dependencies relating to pandas 
pd.show_versions()

# installed version of only pandas
pd.__version__ 

# pandas documentation: pd.<TAB>
# package specific
# pd.read_csv? (warning in Spyder not shown in Jupyter)

# loading datasets
olympics = pd.read_csv('olympics.csv')
codes = pd.read_csv('country_codes.csv')

# showing beginning of file and dropping mistaken column
print(olympics.head())
olympics = olympics.drop([0])
print(olympics)

# Series: 1D Array of Indexed Data; Accessing a Single Series
print()
print(olympics['City']) # or print(olympics.City)
print(olympics['Sport'])

# Series Type
print()
print(type(olympics['City']))

# multiple series
print(olympics[['City','Edition','Athlete']])

# DataFrame work
print(list(olympics))
print(olympics[['Edition','City','Athlete','Medal']])
print(type(olympics[['Edition','City','Athlete','Medal']]))

'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: pd_plotting.py
    
Description: Basic Plotting in Pandas
    
'''
# importing libraries and loading dataset
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
olympics = pd.read_csv('olympics.csv',skiprows=1)

# Plot Types ---------------

# different sports in the first olympics
first = olympics[olympics.Edition == 1896]
first_sports = first.Sport.value_counts()

# creating graph
plt.figure(figsize = (12,8),dpi = 300)
plt.title('Sports Held in the 1896 Summer Olympics')
plt.xlabel('Sport')
plt.ylabel('Count')

# visualizing different sports: line plot
plt.plot(first_sports)

# barplot lists
sports = (['Gymnastics','Athletics','Cycling','Shooting','Aquatics',
            'Tennis','Fencing','Weightlifting','Wrestling'])
medals = (['Silver','Bronze','Gold'])
plt.bar(sports, first_sports)

# # horizontal barplot
plt.barh(sports, first_sports)

# pie chart
plt.pie(first_sports,labels = sports)

# Colors ---------------
plt.plot(first_sports, color = 'plum')
plt.bar(sports, first_sports, color = 'maroon')

# Seaborn Basic Plotting  ---------------

# plotting medals by gender
sns.countplot(x='Medal', data = olympics, hue = 'Gender')

# plotting CHN 2008 medals by gender
china_08 = olympics[(olympics.NOC == 'CHN') & (olympics.Edition == 2008)]
sns.countplot(x='Medal', data = china_08, hue = 'Gender')





import matplotlib.pyplot as plt
import numpy as np

# Easily read a .txt file into a list of numbers
def easyRead(fileName):
    fileIn = open(fileName, "r")
    lstTemStrings = fileIn.read().splitlines()
    lstTemNumbers = [float(item) for item in lstTemStrings]
    return lstTemNumbers

# Generates a list of numbers from 1 to the given value, inclusive
def rangeList(nums):
    return list(range(1, nums + 1))

# Uses two lists to create a simple line graph
def lineGraph(xNums, yNums):
    if len(xNums) == len(yNums):
        plt.plot(xNums, yNums)
    else:
        print("The lists must be the same length")

# Creates a simple bar graph
def barGraph(categories, values):
    if len(categories) == len(values):
        plt.bar(categories, values)
    else:
        print("The lists must be the same length")

# Simple scatter plot
def scatterPlot(xNums, yNums):
    if len(xNums) == len(yNums):
        plt.scatter(xNums, yNums)
    else:
        print("The lists must be the same length")

# Simple pie chart
def simplePie(pops, labels):
    if len(pops) == len(labels):
        plt.pie(pops, labels=labels)
    else:
        print("Number of categories and number of proportions must match")

# Create a 2x2 grid of subplots to display different types of charts

# 1st subplot: Bar graph of colors and their values
plt.subplot(2, 2, 1)
colors = ['Red', 'Blue', 'Purple', 'Pink', 'Cyan', 'Green', 'Brown', 'Orange'] 
values = [3, 3, 3, 2, 1, 2, 2, 1]
plt.bar(colors, values) 
plt.xlabel('Colors') 
plt.ylabel('Values') 
plt.title('Color Bar Graph')

# 2nd subplot: Scatter plot of temperature data over years
plt.subplot(2, 2, 2)
xaxis = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
         '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
         '20', '21', '22', '23', '24']  # Years as strings (short format)
yaxis = [19, 23, 32, 31, 24, 47, 42, 44, 33, 47, 29, 49, 36, 33, 40, 53, 48, 26, 39,
         56, 18, 62, 15, 62, 46]                  # Corresponding temperature values
plt.scatter(xaxis, yaxis)
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Scatter Plot')

# 3rd subplot: Line graph using data read from an external file
plt.subplot(2, 2, 3)
xYears = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
          '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']  # Years as strings (short format)
yPercent = easyRead("lineGraph.txt")  # Reads values from text file
lineGraph(xYears, yPercent)

# 4th subplot: Pie chart of population distribution by generation
plt.subplot(2, 2, 4)
labels = ['Greatest Generation', 'Silent Generation', 'Baby Boomers', 'Millennials',
          'Generation Z', 'Generation X', 'Generation Alpha']
pops = [0.13, 4.92, 20.93, 19.51, 21.71, 20.69, 12.76]  # Population percentages
simplePie(pops, labels)

# Display all the plots together
plt.show()

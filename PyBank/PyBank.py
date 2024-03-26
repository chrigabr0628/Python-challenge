#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd
from pathlib import Path


# In[2]:


pybank_csv = Path("Resources/budget_data.csv")

budget_df = pd.read_csv(pybank_csv)
budget_df.head()


# In[3]:


count = 0
net_total = 0
net_changes = 0 
months = 0


# In[4]:


average_changes = []
dates = []
profit_loses = []
greatest_increase = [0, ""]
greatest_decrease = [9999999999, ""]


# In[5]:


with open(pybank_csv) as pybank_csv_file:
    pybankreader = csv.reader(pybank_csv_file, delimiter=',')
  

    pybank_header = next(pybankreader)
   

    firstrow = next(pybankreader)
    count = count + 1

    net_total = net_total + int(firstrow[1])
    previous_net = int(firstrow[1])
    
    
    
    for row in pybankreader:
        
        
        count = count + 1

        
        dates.append(row[0])

         
        net_total = net_total + int(row[1])
        net_changes = int(row[1]) - previous_net
        

        profit_loses.append(net_changes)
        previous_net = int(row[1])
        

        if net_changes > greatest_increase[0]: 
           greatest_increase[0] = net_changes
           greatest_increase[1] = row[0] 
            
            
        if net_changes < greatest_decrease[0]: 
           greatest_decrease[0] = net_changes
           greatest_decrease[1] = row[0] 

        
average_profit_changes = round(sum(profit_loses)/len(profit_loses), 2)
        
        
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(net_total))
print("Average Change: " + "$" + str(average_profit_changes))
print("Greatest Increase in Profits: " + str(greatest_increase[1]) + " ($" + str(greatest_increase[0]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[1]) + " ($" + str(greatest_decrease[0])+ ")")
print("----------------------------------------------------------")
    


# In[6]:


with open('financial_analysis.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("Financial Analysis" + "\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Months: " + str(count) + "\n")
        text.write("Total Profits: " + "$" + str(net_total) + "\n")
        text.write("Average Change: " + "$" + str((average_profit_changes)) + "\n")
        text.write("Greatest Increase in Profits: " + str(greatest_increase[1]) + " ($" + str(greatest_increase[0]) + ")\n")
        text.write("Greatest Decrease in Profits: " + str(greatest_decrease[1]) + " ($" + str(greatest_decrease[0])+ ")\n")
        text.write("----------------------------------------------------------\n")


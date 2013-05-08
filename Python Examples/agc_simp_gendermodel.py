# A basic model using only an individual's gender as a predictor.
# y=b0+b1(gender)

import csv as csv
import numpy as np
data=[]

with open('train.csv', 'rb') as f: # deals with opening and closing
    csv_file = csv.reader(open('train.csv', 'rb'))
    csv_file.next() # skips the header, so we can get to the data. 
    for row in csv_file: 
        data.append(row) 

# Then we convert  our list to NumPy array for more efficient data manipulation. 
data = np.array(data) 

#Separates data by gender
women_only_stats = data[0::,3] == "female" 
men_only_stats = data[0::,3] != "female"


# Calculates survival proportions by gender
women_onboard = data[women_only_stats,0].astype(np.float)
men_onboard = data[men_only_stats,0].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
proportion_survivors =  (np.sum(data[0::,0].astype(np.float)))/(np.size(data[0::,0].astype(np.float)))

                         
# Prints proportions
print 'Proportion of people who survived is %s' % proportion_survivors
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

# Reads in the 'train' file for a comparative result
with open('train.csv', 'rb') as f2:
    f2.next() # Skips header 
    cop_open_file=open("train_results_genderbasedmodelpy.csv", "wb")
    open_file=csv.writer(cop_open_file) #theres no header in this guy
    for row in csv.reader(f2):
        if row[3] == 'female':
            print row[3]
            row[0]='1' #Insert the prediction at the start of the row
            open_file.writerow(row) #Write the row to the file
        else:
            print row[3]
            row[0]='0'
            open_file.writerow(row)
    cop_open_file.close()

print "Analysis ended"

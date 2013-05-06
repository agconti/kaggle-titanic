###basic model as bench mark
###y=b0+b1(gender)

import csv as csv
import numpy as np
data=[]

with open('train.csv', 'rb') as f: #deals with opening and closing
    csv_file = csv.reader(open('train.csv', 'rb'))
    #csv_file.next()#skips the header, so we can manipulate ##I deleted this sucker, my bad.
    for row in csv_file: 
        data.append(row) 

#Then convert from a list to an array
data = np.array(data) 
###Done With Data Prep############


#seperates data by gender
women_only_stats = data[0::,3] == "female" 
men_only_stats = data[0::,3] != "female"


#finds proportions
women_onboard = data[women_only_stats,0].astype(np.float)
men_onboard = data[men_only_stats,0].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
proportion_survivors =  (np.sum(data[0::,0].astype(np.float)))/(np.size(data[0::,0].astype(np.float)))

                         
#prints proportions
print 'Proportion of people who survived is %s' % proportion_survivors
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

##reads in the 'train' file for a comparative result
with open('train.csv', 'rb') as f2:
    ##f2.next()#skip header ##I deleted the header
    cop_open_file=open("train_results_genderbasedmodelpy.csv", "wb")
    open_file=csv.writer(cop_open_file) #theres no header in this guy
    for row in csv.reader(f2):
        if row[3] == 'female':
            print row[3]
            row[0]='1' #Insert the prediciton at the start of the row
            open_file.writerow(row) #Write the row to the file
        else:
            print row[3]
            row[0]='0'
            open_file.writerow(row)
    cop_open_file.close()



##with open('train.csv', 'rb') as f2:
##    test_file = csv.reader(open('test.csv', 'rb'))
##    test_file.next()#skip header
##    with open("train_results_genderbasedmodelpy.csv", "wb") as f3: #theres no header in this guy
##        open_file = csv.writer(open("train_results_genderbasedmodelpy.csv", "wb"))
##        for row in test_file:
##            if row[2] == 'female':
##                row.insert(0,'1') #Insert the prediciton at the start of the row
##                open_file.writerow(row) #Write the row to the file
##            else:
##                row.insert(0,'0')
##                open_file.writerow(row)

###reads in the test file, this outputs results for final submission
##with open('test.csv', 'rb') as f2:
##    test_file = csv.reader(open('test.csv', 'rb'))
##    test_file.next()#skip header
##    with open("genderbasedmodelpy.csv", "wb") as f3: #theres no header in this guy
##        open_file = csv.writer(open("genderbasedmodelpy.csv", "wb"))
##        for row in test_file:
##            if row[2] == 'female':
##                row.insert(0,'1') #Insert the prediciton at the start of the row
##                open_file.writerow(row) #Write the row to the file
##            else:
##                row.insert(0,'0')
##                open_file.writerow(row)
##
##

print "Analysis ended"

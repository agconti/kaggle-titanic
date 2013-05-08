#RandomForest, non parametric modeling
#agconti

import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier


train_data=[] # Create a bin to hold our training data.
test_data=[]  # Create a bin to hold our test data.

# Read in CSVs, train and test

with open('train.csv', 'rb') as f1:
    header = csv_file_object.next()
    for row in  csv.reader(f1):       # Skip through each row in the csv file
        train_data.append(row)        # Add each row to the data variable
    train_data = np.array(train_data) # Then convert from a list to a NumPy array

with open('test.csv', 'rb') as f2:  # Load in the test csv file
    f2.next()                       # Skip the fist line because it is a header
    for row in csv.reader(f2):      # Skip through each row in the csv file
        test_data.append(row)       # Add each row to the data variable
    test_data = np.array(test_data) # Then convert from a list to an array

# Convert strings to numbers so we can perform computational analysis    
# The gender classifier in column 3: Male = 1, female = 0:
train_data[train_data[0::,3] == 'male', 3] = 1
train_data[train_data[0::,3] == 'female', 3] = 0

# Embark C = 0, S = 1, Q = 2
train_data[train_data[0::,10] == 'C', 10] = 0
train_data[train_data[0::,10] == 'S', 10] = 1
train_data[train_data[0::,10] == 'Q', 10] = 2

# Transfer Null observations
# So where there is no price, I will assume price on median of that class
# Where there is no age I will give median of all ages

# All the ages with no data make the median of the data
train_data[train_data[0::,4] == '',4] = np.median(train_data[train_data[0::,4]\
                                           != '',4].astype(np.float))
# All missing embarks just make them embark from most common place
train_data[train_data[0::,10] == '',10] = np.round(np.mean(train_data[train_data[0::,10]\
                                                   != '',10].astype(np.float)))

train_data = np.delete(train_data,[2,7,9],1) #remove the name data, cabin and ticket
# I need to do the same with the test data now so that the columns are in the same
# as the training data



# I need to convert all strings to integer classifiers:
# male = 1, female = 0:
test_data[test_data[0::,2] == 'male',2] = 1
test_data[test_data[0::,2] == 'female',2] = 0

# Embark C = 0, S = 1, Q = 2
test_data[test_data[0::,9] == 'C',9] = 0 
test_data[test_data[0::,9] == 'S',9] = 1
test_data[test_data[0::,9] =='Q',9] = 2

# All the ages with no data make the median of the data
test_data[test_data[0::,3] == '',3] = np.median(test_data[test_data[0::,3]\
                                           != '',3].astype(np.float))
# All missing embarks just make them embark from most common place
test_data[test_data[0::,9] == '',9] = np.round(np.median(test_data[test_data[0::,9]\
                                                   != '',9].astype(np.float)))
# All the missing prices assume median of their respective class
for i in xrange(np.size(test_data[0::,0])):
    if test_data[i,7] == '':
        test_data[i,7] = np.median(test_data[(test_data[0::,7] != '') &\
                                             (test_data[0::,0] == test_data[i,0])\
            ,7].astype(np.float))

test_data = np.delete(test_data,[1,6,8],1) # Remove the name data, cabin and ticket


# The data is now ready to go. So lets train then test!

print 'Training '
forest = RandomForestClassifier(n_estimators = 1000)

forest = forest.fit(train_data[0::,1::],\
                    train_data[0::,0])

print 'Predicting'
output = forest.predict(test_data) #predict results using our CLEANED data


# Write Results to fie
# open csv
seedling=open("agcfirstforest.csv", "wb")
test=open('test.csv', 'rb')
forest_Csv = csv.writer(seedling)
test_file_object = csv.reader(test) 

test_file_object.next() # Header control

i = 0
for row in test_file_object:
    row.insert(0,output[i].astype(np.uint8))
    forest_Csv.writerow(row)
    i += 1
 
test.close()
seedling.close()

print "Analysis has Finished"

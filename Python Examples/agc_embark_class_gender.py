# A model for prediction survival on the Titianic based on where an 
# induvidual Embarked, thier gender, or the class they travled in. 
# AGC 2013
# 
# 
# Here Will will run generate predictions of who survived and who did not
# from our basic Least Squares Regression model.
# Our Formula is :
# survived_prediction=(C+(b1female)+(b2U_Class)+(b3embarked_c))

# Import utilites
import csv as csv
import numpy as np

# declare nessesary variables
data = [] # a contianer to hold our test data in.
x =  0

# Regression Variables
# independent variables, (what we are trying to predict)
survived_prediction=0 # We intialize this variale as zero as a place holder

# dependent variables, (what we are using to make our predictions)
# These are the coefficents we gained from training our OLS regerssion on 
# the training data.

C = float(0.077158358)
U_ Class = float(0.234214501)
female = float(0.512110314)
embarked_c = float(0.111687285)

# The file is already trained on the train.csv file. 
# Now we test our model by making predctions on the test.csv file. 
# You'll notice the test.csv file has no values in the survived field. This
# Is what wer are tying to predict. 

with open('test2.csv', 'rb') as f: # Handels the opening and closing of the file for us.
    csv_file = csv.reader(open('test2.csv', 'rb'))
    csv_file.next() # skips the header in the test file, so we can get right to the data
    for row in csv_file: 
        data.append(row) 
    data = np.array(data)

print "\nBegin Predictions:"


# reads in the 'train' file for a comparative result
cop_open_file = open("pred_embarkclassgendermodel.csv", "wb") # opens the file with write privilages ("wb")
open_file = csv.writer(cop_open_file) # Theres no header in this guy

with open('test2.csv', 'rb') as f: # Handels the opening and closing of the file for us.
    csv_file = csv.reader(open('test2.csv', 'rb'))
    csv_file.next()
    
    for row in csv_file:
        surived_pred = (C + (female * int(data[x][1])) + (U_Class * int(data[x][0])) + (embarked_c * int(data[x][2])))
        
        print "Row #:" + str(x)
        print "urvived_pred: " + str(urvived_pred) + "         female: %s  Class: %s  Em: %s" %(data[x][1],data[x][0],data[x][2])
        
        if survived_prediction > .50000:
            pred_val = 1
        else:
            pred_val = 0
        row.insert(0,pred_val) #Insert the prediciton at the start of the row
        open_file.writerow(row) #Write the row to the file
        x += 1

cop_open_file.close()

print "Analysis ended"

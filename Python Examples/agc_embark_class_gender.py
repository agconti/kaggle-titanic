# A model for prediction survival on the Titanic based on where an 
# individual Embarked, their gender, or the class they traveled in. 
# AGC 2013
# 
# 
# Here Will will run generate predictions of who survived and who did not
# from our basic Least Squares Regression model.
# Our Formula is :
# survived_prediction = C + (b1 * female) + (b2 * U_Class) + (b3 * embarked_c))

# Import Utilities
import csv as csv
import numpy as np

# declare necessary variables
data = []   # a container to hold our test data in.
x =  0      # a container for an iterator later on 

# Regression Variables
# independent variables, (what we are trying to predict)
survived_prediction=0 # We initialize this variable as zero as a place holder

# dependent variables, (what we are using to make our predictions)
# These are the coefficients we gained from training our OLS regression on 
# the training data.

C = float(0.077158358)
U_ Class = float(0.234214501)
female = float(0.512110314)
embarked_c = float(0.111687285)

# The file is already trained on the train.csv file. 
# Now we test our model by making predictions on the test.csv file. 
# You'll notice the test.csv file has no values in the survived field. This
# Is what we're are tying to predict. 

with open('test.csv', 'rb') as f:                  # Handel's the opening and closing of the file for us.
    csv_file = csv.reader(open('test.csv', 'rb'))
    csv_file.next()                                 # Skips the header in the test file, so we can get right to the data
    for row in csv_file: 
        data.append(row) 
    data = np.array(data)

# The print statements used throughout are designed to show what the program is doing
# Once its executed in the terminal. 
# The \n starts a new line. This allows for more attractive printing.  
print "\nBegin Predictions:" 


# Reads in the 'train' file for a comparative result
cop_open_file = open("results_embarkclassgendermodel.csv", "wb")    # Creates a csv file with write privileges ("wb") called
                                                                    # results_embarkclassgendermodel.csv
open_file = csv.writer(cop_open_file)                               # Theres no header in this guy

with open('test.csv', 'rb') as f:                                   # Handel's the opening and closing of the file for us.
    csv_file = csv.reader(open('test.csv', 'rb'))
    csv_file.next()
    
    for row in csv_file:
        surived_pred = (C + (female * int(data[x][1])) + (U_Class * int(data[x][0])) + (embarked_c * int(data[x][2])))
        
        print "Row #:" + str(x)
        print "urvived_pred: " + str(urvived_pred) + "         female: %s  Class: %s  Em: %s" %(data[x][1],data[x][0],data[x][2])
        
        if survived_prediction > .50000:
            pred_val = 1
        else:
            pred_val = 0
        row.insert(0,pred_val)  # Insert the prediction at the start of the row
        open_file.writerow(row) # Write the row to the file
        x += 1

cop_open_file.close()

print "Analysis ended"

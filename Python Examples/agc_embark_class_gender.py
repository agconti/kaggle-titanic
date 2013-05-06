###Embark,gender, class model
###sur_pred=(C+(b1female)+(b2U_Class)+(b3embarked_c))

import csv as csv
import numpy as np
data=[]
x=0
####Regression Vars#######
#indpendent
sur_pred=0
#dependent
C=float(0.077158358)
U_Class=float(0.234214501)
female=float(0.512110314)
embarked_c=float(0.111687285)
#file is already trained

with open('test2.csv', 'rb') as f: #deals with opening and closing
    csv_file = csv.reader(open('test2.csv', 'rb'))
    csv_file.next()#skips the header, so we can manipulate ##I deleted this sucker, my bad.
    for row in csv_file: 
        data.append(row) 
    data=np.array(data)

print "\nBegin Predictions:"


##reads in the 'train' file for a comparative result
cop_open_file=open("pred_embarkclassgendermodel.csv", "wb")
open_file=csv.writer(cop_open_file) #theres no header in this guy
with open('test2.csv', 'rb') as f: #deals with opening and closing
    csv_file = csv.reader(open('test2.csv', 'rb'))
    csv_file.next()
    for row in csv_file:
        sur_pred=(C+(female*int(data[x][1]))+(U_Class*int(data[x][0]))+(embarked_c*int(data[x][2])))
        print "Row #:"+str(x)
        print "sur_pred: "+str(sur_pred)+"         female: %s  Class: %s  Em: %s" %(data[x][1],data[x][0],data[x][2])
        if sur_pred>.50000:
            pred_val=1
        else:
            pred_val=0
        row.insert(0,pred_val) #Insert the prediciton at the start of the row
        open_file.writerow(row) #Write the row to the file
        x+=1

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

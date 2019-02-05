import pandas as pd

#Defining function to check for digit input and if the input is between the desired numbers and converting the string input to integer input if the first two conditions are met.

def int_check(l,h,message):
    while True:
        s = input(message)
        if s.isdigit():
            s=int(s)
            if l<=s<=h:
                return s
            else:
                print("\nError in input, please try again.")
        else:
            print("\nError in input, please try again.")

#Defining function to read csv, print it, take input for prediction, if yes, predict and show value for next year.

def csv_display(directory,index,z):
    s = pd.read_csv(directory)
    print(s)
    o = int_check(1,2,"\nWould you like to predict future values?\n\n1. Yes\n2. No\n\nChoose a corresponding number: ")
    if o==1:
        n = int_check(0,36,'\nWhich one of the following places would you like to predict the future values for?\n\n{}\n\nPlease choose the corresponding integer: '.format(s.iloc[:,0].to_string()))
        mean = s[index].mean(axis=1)
        std = s[index].std(axis=1)
        lower = mean - std
        upper = mean + std
        i=0
        for i in range(0,37):
            if n==i:
                print('\nThe range of values for',s.iloc[i][0],'are between',lower.iloc[i],'and',upper.iloc[i],'for the year',z)
                i=i+1
    return s

# a variable is to decide initial dataset, b variable is for selecting the dataset within the dataset, c is sub-choice.

print("\nPlease choose which Dataset you'd like to access, view or predict future values of:\n1. Education\n2. Demography\n3. Economy\n4. Industries\n5. Transport\n6. Labour & Employment")
a = int_check(1,6,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 6, inclusive): ")
if a==1:
    print("\nPlease input the value correcponding to the Idicator in the 'Education' dataset you'd like to view:\n1. Gross Enrolment Ratio in Higher Education\n2. Literacy Rate (7+ Years)\n3. Percentage Of Schools With Electricity\n4. Percentage Of Schools With Girls Toilet\n5. Percentage Of Schools With Boys Toilet\n6. Percentage Of Schools With Drinking Water\n7. Gross Enrolment Ratio In Schools\n8. Percentage Of Schools With Computers\n9. Drop-Out Rate")
    b = int_check(1,9,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 9, inclusive): ")
    if b==1:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n1. Female \n2. Male\n3. Total\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Female.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.')
        elif c==2:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Male.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.')
        elif c==3:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Total.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.')
    elif b==2:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n1. Rural\n2. Total\n3. Urban\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/LR_Rural.csv',['2001','2011'],'2021.')
        elif c==2:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/LR_Total.csv',['2001','2011'],'2021.')
        elif c==3:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/LR_Urban.csv',['2001','2011'],'2021.')
    elif b==3:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n1. All Schools\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/SWE_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.')
    elif b==4:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n1. All Schools\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/SGT_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.')
    elif b==5:
        print('\nYet to code.')
    elif b==6:
        print('\nYet to code.')
    elif b==7:
        print('\nYet to code.')
    elif b==8:
        print('\nYet to code.')
    elif b==9:
        print('\nYet to code.')
elif a==2:
    print("\nPlease input the value correcponding to the Idicator in the 'Demography' dataset you'd like to view:\n1. Child Sex Ratio (0-6 Years)\n2. Sex Ratio\n3. Decadal Growth Rate")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        print('\nYet to code.')
    elif b==2:
        print('\nYet to code.')
    elif b==3:
        print('\nYet to code.')
elif a==3:
    print("\nPlease input the value correcponding to the Idicator in the 'Economy' dataset you'd like to view:\n1. Gross Domestic Product (GDP) At Current Price\n2. Gross Domestic Product (GDP) At Constant Price\n3. State-Wise Net Domestic Product (NDP) At Current Price\n4. State-Wise Net Domestic Product (NDP) At Constant Price")
    b = int_check(1,4,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
    if b==1:
        print('\nYet to code.')
    elif b==2:
        print('\nYet to code.')
    elif b==3:
        print('\nYet to code.')
    elif b==4:
        print('\nYet to code.')
elif a==4:
    print("\nPlease input the value correcponding to the Idicator in the 'Industries' dataset you'd like to view:\n1. Foreign Direct Investment (FDI) Equity Inflows In Machinery\n2. Foreign Direct Investment (FDI) In Agriculture\n3. Foreign Direct Investment (FDI) Equity Inflows")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        print('\nYet to code.')
    elif b==2:
        print('\nYet to code.')
    elif b==3:
        print('\nYet to code.')
elif a==5:
    print("\nPlease input the value correcponding to the Idicator in the 'Transport' dataset you'd like to view:\n1. Total Road Length By Category Of Roads\n2. Total And Surfaced Length Of Rural Roads\n3. Length Of National Highways")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        print('\nYet to code.')
    elif b==2:
        print('\nYet to code.')
    elif b==3:
        print('\nYet to code.')
elif a==6:
    print("\nPlease input the value correcponding to the Idicator in the 'Labour & Employment' dataset you'd like to view:\n1. Changes In Employment In Selected Sectors\n2. State-Wise Unemployment Rate (Per 1000)\n3. State-Wise Labour Force Participation Rate (Per 1000)\n4. State-Wise Worker Population Ratio (Per 1000)")
    b = int_check(1,4,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
    if b==1:
        print('\nYet to code.')
    elif b==2:
        print('\nYet to code.')
    elif b==3:
        print('\nYet to code.')
    elif b==4:
        print('\nYet to code.')
print("\nThank you for using this program made by Digvijay Ghotane during the academic year 2018-19.")
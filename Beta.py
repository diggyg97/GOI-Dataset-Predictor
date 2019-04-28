import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

def csv_display(directory,index,z,x):
    s = pd.read_csv(directory)
    print(s)
    o = int_check(1,2,"\nWould you like to predict future values?\n\n1. Yes\n2. No\n\nChoose a corresponding number: ")
    #If loop here exists for datasets that do not have more than 1 column of values.
    if directory not in ['Datasets/Transport/TS.csv','Datasets/LAE/UR.csv','Datasets/LAE/LFPR.csv','Datasets/LAE/WRP.csv']:
        if o==1:
            n = int_check(0,x,'\nWhich one of the following places would you like to predict the future values for?\n\n{}\n\nPlease choose the corresponding integer: '.format(s.iloc[:,0].to_string()))
            mean = s[index].mean(axis=1)
            std = s[index].std(axis=1)
            lower = mean - std
            upper = mean + std
            i=0
            for i in range(0,x+1):
                if n==i:
                    if lower.iloc[i]>100 and directory not in ['Datasets/Education/GERP.csv','Datasets/Education/GERUP.csv','Datasets/Education/GERS.csv','Datasets/Education/GERUS.csv','Datasets/Demography/CSR_Rural.csv','Datasets/Demography/CSR_Total.csv','Datasets/Demography/CSR_Urban.csv','Datasets/Demography/SR_Rural.csv','Datasets/Demography/SR_Total.csv','Datasets/Demography/SR_Urban.csv','Datasets/Demography/DC_Rural.csv','Datasets/Demography/DC_Total.csv','Datasets/Demography/DC_Urban.csv','Datasets/Economy/PGOY.csv','Datasets/Economy/GSDP_2.csv','Datasets/Economy/NSDP_2.csv','Datasets/Economy/NSDP.csv','Datasets/Industries/IMS.csv','Datasets/Industries/MTS.csv','Datasets/Industries/AS.csv','Datasets/Industries/AMS.csv','Datasets/Industries/AS_2.csv','Datasets/Industries/TFS.csv','Datasets/Transport/Roads.csv','Datasets/Transport/NH.csv']:
                        lower.iloc[i]=100
                    if lower.iloc[i]<0:
                        lower.iloc[i]=0
                    if upper.iloc[i]>100 and directory not in ['Datasets/Education/GERP.csv','Datasets/Education/GERUP.csv','Datasets/Education/GERS.csv','Datasets/Education/GERUS.csv','Datasets/Demography/CSR_Rural.csv','Datasets/Demography/CSR_Total.csv','Datasets/Demography/CSR_Urban.csv','Datasets/Demography/SR_Rural.csv','Datasets/Demography/SR_Total.csv','Datasets/Demography/SR_Urban.csv','Datasets/Demography/DC_Rural.csv','Datasets/Demography/DC_Total.csv','Datasets/Demography/DC_Urban.csv','Datasets/Economy/PGOY.csv','Datasets/Economy/GSDP_2.csv','Datasets/Economy/NSDP_2.csv','Datasets/Economy/NSDP.csv','Datasets/Industries/IMS.csv','Datasets/Industries/MTS.csv','Datasets/Industries/AS.csv','Datasets/Industries/AMS.csv','Datasets/Industries/AS_2.csv','Datasets/Industries/TFS.csv','Datasets/Transport/Roads.csv','Datasets/Transport/NH.csv']:
                        upper.iloc[i]=100
                    if upper.iloc[i]<0:
                        upper.iloc[i]=0
                    print('\nThe range of values for',s.iloc[i][0],'are between',round(lower.iloc[i],3),'and',round(upper.iloc[i],3),'for',z)
                    i=i+1
    else:
        print("\nYou cannot predict values for this particular dataset.")
    o = int_check(1,2,"\nWould you like to see a graphical representation?\n\n1. Yes\n2. No\n\nChoose a corresponding number: ")
    if o==1:
        n = int_check(0,x,'\nWhich one of the following places would you like to graphically represent?\n\n{}\n\nPlease choose the corresponding integer: '.format(s.iloc[:,0].to_string()))
        h = index
        j = s.iloc[n,1:]
        plt.scatter(h,j)
        plt.xlabel('Year')
        plt.ylabel('Values')
        plt.show()
    return s

# a variable is to decide initial dataset, b variable is for selecting the dataset within the dataset, c is sub-choice.

print("\nPlease choose which Dataset you'd like to access, view or predict future values of:\n1. Education\n2. Demography\n3. Economy\n4. Industries\n5. Transport\n6. Labour & Employment")
a = int_check(1,6,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 6, inclusive): ")
if a==1:
    print("\nPlease input the value correcponding to the Idicator in the 'Education' dataset you'd like to view:\n\n1. Gross Enrolment Ratio in Higher Education\n2. Literacy Rate (7+ Years)\n3. Percentage Of Schools With Electricity\n4. Percentage Of Schools With Girls Toilet\n5. Percentage Of Schools With Boys Toilet\n6. Percentage Of Schools With Drinking Water\n7. Gross Enrolment Ratio In Schools\n8. Percentage Of Schools With Computers\n9. Drop-Out Rate")
    b = int_check(1,9,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 9, inclusive): ")
    if b==1:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Female \n2. Male\n3. Total\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/GERH_Female.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.',36)
        elif c==2:
            d = csv_display('Datasets/Education/GERH_Male.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.',36)
        elif c==3:
            d = csv_display('Datasets/Education/GERH_Total.csv',['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16'],'2016-17.',36)
    elif b==2:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Rural\n2. Total\n3. Urban\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/LR_Rural.csv',['2001','2011'],'2021.',36)
        elif c==2:
            d = csv_display('Datasets/Education/LR_Total.csv',['2001','2011'],'2021.',36)
        elif c==3:
            d = csv_display('Datasets/Education/LR_Urban.csv',['2001','2011'],'2021.',36)
    elif b==3:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. All Schools\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/SWE_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==4:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. All Schools\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/SGT_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==5:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. All Schools\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/SBT_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==6:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. All Schools\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/DWF_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==7:
        c = int_check(1,4,"\nWhich DataSet do you want to access?\n\n1. Primary\n2. Upper Primary\n3. Secondary\n4. Upper Secondary\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/GERP.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
        if c==2:
            d = csv_display('Datasets/Education/GERUP.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
        if c==3:
            d = csv_display('Datasets/Education/GERS.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
        if c==4:
            d = csv_display('Datasets/Education/GERUS.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==8:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. All Schools\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/SWC_Total.csv',['2013-14','2014-15','2015-16'],'2016-2017.',36)
    elif b==9:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Primary Total\n2. Secondary Total\n3. Higher Secondary Total\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Education/DOR_Primary_Total.csv',['2012-13','2013-14','2014-15'],'2015-2016.',36)
        if c==2:
            d = csv_display('Datasets/Education/DOR_Secondary_Total.csv',['2012-13','2013-14','2014-15'],'2015-2016.',36)
        if c==3:
            d = csv_display('Datasets/Education/DOR_Higher_Secondary_Total.csv',['2012-13','2013-14','2014-15'],'2015-2016.',36)
elif a==2:
    print("\nPlease input the value correcponding to the Idicator in the 'Demography' dataset you'd like to view:\n1. Child Sex Ratio (0-6 Years)\n2. Sex Ratio\n3. Decadal Growth Rate")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Rural\n2. Total\n3. Urban\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Demography/CSR_Rural.csv',['2001','2011'],'2021.',36)
        elif c==2:
            d = csv_display('Datasets/Demography/CSR_Total.csv',['2001','2011'],'2021.',36)
        elif c==3:
            d = csv_display('Datasets/Demography/CSR_Urban.csv',['2001','2011'],'2021.',36)
    elif b==2:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Rural\n2. Total\n3. Urban\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Demography/SR_Rural.csv',['2001','2011'],'2021.',36)
        elif c==2:
            d = csv_display('Datasets/Demography/SR_Total.csv',['2001','2011'],'2021.',36)
        elif c==3:
            d = csv_display('Datasets/Demography/SR_Urban.csv',['2001','2011'],'2021.',36)
    elif b==3:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Rural\n2. Total\n3. Urban\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Demography/DC_Rural.csv',['1991-01','2001-11'],'2011-21.',36)
        elif c==2:
            d = csv_display('Datasets/Demography/DC_Total.csv',['1991-01','2001-11'],'2011-21.',36)
        elif c==3:
            d = csv_display('Datasets/Demography/DC_Urban.csv',['1991-01','2001-11'],'2011-21.',36)
elif a==3:
    print("\nPlease input the value correcponding to the Idicator in the 'Economy' dataset you'd like to view:\n1. Gross Domestic Product (GDP) At Current Price\n2. Gross Domestic Product (GDP) At Constant Price\n3. State-Wise Net Domestic Product (NDP) At Current Price\n4. State-Wise Net Domestic Product (NDP) At Constant Price")
    b = int_check(1,4,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
    if b==1:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. State Wise Gross Domestic Product - Current Prices \n2. Percentage Growth Over Previous Year\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Economy/GSDP.csv',['2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
        elif c==2:
            d = csv_display('Datasets/Economy/PGOY.csv',['2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
    elif b==2:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. State Wise Gross Domestic Product - Constant Prices \n2. Percentage Growth Over Previous Year\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Economy/GSDP_2.csv',['2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
        elif c==2:
            d = csv_display('Datasets/Economy/PGOY_2.csv',['2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
    elif b==3:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. State Wise Net Domestic Product - Current Prices \n2. Percentage Growth Over Previous Year\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Economy/NSDP.csv',['2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
        elif c==2:
            d = csv_display('Datasets/Economy/PGOY_3.csv',['2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
    elif b==4:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. State Wise Net Domestic Product - Constant Prices \n2. Percentage Growth over previous year\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Economy/NSDP_2.csv',['2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
        elif c==2:
            d = csv_display('Datasets/Economy/PGOY_4.csv',['2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',33)
elif a==4:
    print("\nPlease input the value correcponding to the Idicator in the 'Industries' dataset you'd like to view:\n1. Foreign Direct Investment (FDI) Equity Inflows In Machinery\n2. Foreign Direct Investment (FDI) In Agriculture\n3. Foreign Direct Investment (FDI) Equity Inflows")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. Industrial Machinery Sector\n2. Machine Tools Sector\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Industries/IMS.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
        elif c==2:
            d = csv_display('Datasets/Industries/MTS.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
    elif b==2:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. Agriculture Services\n2. Agricultural Machinery Sector\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Industries/AS.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
        elif c==2:
            d = csv_display('Datasets/Industries/AMS.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
    elif b==3:
        c = int_check(1,2,"\nWhich DataSet do you want to access?\n\n1. Agriculture Services\n2. Top 5 Sectors\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Industries/AS_2.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
        elif c==2:
            d = csv_display('Datasets/Industries/TFS.csv',['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17'],'2017-18.',63)
elif a==5:
    print("\nPlease input the value correcponding to the Idicator in the 'Transport' dataset you'd like to view:\n1. Total Road Length By Category Of Roads\n2. Total And Surfaced Length Of Rural Roads\n3. Length Of National Highways")
    b = int_check(1,3,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
    if b==1:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. Road length by Category in India from 2001 to 2015\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Transport/Roads.csv',['1951','1961','1971','1981','1991','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015'],'2016.',17)
    elif b==2:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. Total and Surfaced Length of Rural Roads in India as on 31st March 2015\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Transport/TS.csv',['Total','Surfaced'],"doesn't matter",31)
    elif b==3:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. Length of National Highways in India from 2004 to 2015\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/Transport/NH.csv',['2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015'],"2016",36)
elif a==6:
    print("\nPlease input the value correcponding to the Idicator in the 'Labour & Employment' dataset you'd like to view:\n1. Changes In Employment In Selected Sectors\n2. State-Wise Unemployment Rate (Per 1000)\n3. State-Wise Labour Force Participation Rate (Per 1000)\n4. State-Wise Worker Population Ratio (Per 1000)")
    b = int_check(1,4,"\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
    if b==1:
        c = int_check(1,3,"\nWhich DataSet do you want to access?\n\n1. Primary\n2. Secondary\n3. Teritary\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/LAE/Pri.csv',['2009-10','2011-12'],'2013-14.',35)
        elif c==2:
            d = csv_display('Datasets/LAE/Sec.csv',['2009-10','2011-12'],'2013-14.',35)
        elif c==3:
            d = csv_display('Datasets/LAE/Ter.csv',['2009-10','2011-12'],'2013-14.',35)
    elif b==2:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. State-wise Unemployment Rate (per 1000) during 2011-12\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/LAE/UR.csv',['Unemployment Rate'],'doesnt matter',35)
    elif b==3:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. State-wise Labour Force Participation Rate (per 1000) during 2011-12\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/LAE/LFPR.csv',['Labour Force Participation Rate'],'doesnt matter',35)
    elif b==4:
        c = int_check(1,1,"\nWhich DataSet do you want to access?\n\n1. State-wise Worker Population Ratio (per 1000) during 2011-12\n\nPlease choose the corresponding number: ")
        if c==1:
            d = csv_display('Datasets/LAE/WRP.csv',['Worker Population Ratio'],'doesnt matter',35)
print("\nThank you for using this program made by Digvijay Ghotane during the academic year 2018-19.")
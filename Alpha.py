import pandas as pd
import numpy as np

print("\nPlease choose which Dataset you'd like to access, view or predict future values of:\n1. Education\n2. Demography\n3. Economy\n4. Industries\n5. Transport\n6. Labour & Employment")
# First Input
while True:
	s = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 6, inclusive): ")
	check_int(s)
	if s.isdigit():
		s = int(s)
		if s == 1:
			print("\nPlease input the value correcponding to the Idicator in the 'Education' dataset you'd like to view:\n1. Gross Enrolment Ratio in Higher Education\n2. Literacy Rate (7+ Years)\n3. Percentage Of Schools With Electricity\n4. Percentage Of Schools With Girls Toilet\n5. Percentage Of Schools With Boys Toilet\n6. Percentage Of Schools With Drinking Water\n7. Gross Enrolment Ratio In Schools\n8. Percentage Of Schools With Computers\n9. Drop-Out Rate")
			while True:
				a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 9, inclusive): ")
				if a.isdigit():
					a = int(a)
					if a == 1:
						while True:
							b = input('\nWhich DataSet do you want to access?\n1. Female \n2. Male\n3. Total\nPlease choose the corresponding number: ')
							if b.isdigit():
								b=int(b)
								if b==1:
									with open('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Female.csv','r') as g:
									print(g.read())
								elif b==2:
									with open('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Male.csv','r') as g:
									print(g.read())
								elif b==3:
									with open('/Users/digvijayghotane/Desktop/Personal_Projects/Data_Analysis_GOI/Datasets/Education/GERH_Total.csv','r') as g:
									print(g.read())
								else:
									print('\nError in input, please try again.')
							else:
								print('Error in input, please try again.')
						elif a==2:
							print('Yet to code.')
						elif a==3:
							print('my nigga')
						elif a==4:
							print('my nigga')
						elif a==5:
							print('my nigga')
						elif a==6:
							print('my nigga')
						elif a==7:
							print('my nigga')
						elif a==8:
							print('my nigga')
						elif a==9:
							print('my nigga')
						else:
							print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')	
	elif s==2:
		print("\nPlease input the value correcponding to the Idicator in the 'Demography' dataset you'd like to view:\n1. Child Sex Ratio (0-6 Years)\n2. Sex Ratio\n3. Decadal Growth Rate")
		a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
		if a.isdigit():
			a=int(a)
			if a==1:
				print('my nigga')
			elif a==2:
				print('my nigga')
			elif a==3:
				print('my nigga')
			else:
				print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')
	elif s==3:
		print("\nPlease input the value correcponding to the Idicator in the 'Economy' dataset you'd like to view:\n1. Gross Domestic Product (GDP) At Current Price\n2. Gross Domestic Product (GDP) At Constant Price\n3. State-Wise Net Domestic Product (NDP) At Current Price\n4. State-Wise Net Domestic Product (NDP) At Constant Price")
		a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
		if a.isdigit():
			a=int(a)
			if a==1:
				print('my nigga')
			elif a==2:
				print('my nigga')
			elif a==3:
				print('my nigga')
			elif a==4:
				print('my nigga')
			else:
				print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')
	elif s==4:
		print("\nPlease input the value correcponding to the Idicator in the 'Industries' dataset you'd like to view:\n1. Foreign Direct Investment (FDI) Equity Inflows In Machinery\n2. Foreign Direct Investment (FDI) In Agriculture\n3. Foreign Direct Investment (FDI) Equity Inflows")
		a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
		if a.isdigit():
			a=int(a)
			if a==1:
				print('my nigga')
			elif a==2:
				print('my nigga')
			elif a==3:
				print('my nigga')
			else:
				print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')	
	elif s==5:
		print("\nPlease input the value correcponding to the Idicator in the 'Transport' dataset you'd like to view:\n1. Total Road Length By Category Of Roads\n2. Total And Surfaced Length Of Rural Roads\n3. Length Of National Highways")
		a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 3, inclusive): ")
		if a.isdigit():
			a=int(a)
			if a==1:
				print('my nigga')
			elif a==2:
				print('my nigga')
			elif a==3:
				print('my nigga')
			else:
				print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')
	elif s==6:
		print("\nPlease input the value correcponding to the Idicator in the 'Labour & Employment' dataset you'd like to view:\n1. Changes In Employment In Selected Sectors\n2. State-Wise Unemployment Rate (Per 1000)\n3. State-Wise Labour Force Participation Rate (Per 1000)\n4. State-Wise Worker Population Ratio (Per 1000)")
		a = input("\nEnter an integer corresponding to the above choice of Indicators (between 1 & 4, inclusive): ")
		if a.isdigit():
			a=int(a)
			if a==1:
				print('my nigga')
			elif a==2:
				print('my nigga')
			elif a==3:
				print('my nigga')
			elif a==4:
				print('my nigga')
			else:
				print('\nError in input, please try again.')
		else:
			print('\nError in input, please try again.')
	else:
		print('\nError in input, please try again.')
else:
	print('\nError in input, please try again.')

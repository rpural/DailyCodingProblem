#! /usr/bin/env python3

'''
    Example of reading and writing an Excel spreadsheet.
    Data file is CustomerSample.xlsx.
'''

import pandas as pd

# Read the file
# customer_sample_file = pd.read_excel("CustomerSample.xlsx", 
customer_sample_file = pd.read_excel("https://lovespreadsheet-tutorials.s3.amazonaws.com/CustomerSample.xlsx",
        sheet_name="Prospects", 
        parse_dates=[0])

# Get records from 2017 or earlier
customers_2017_or_earlier = customer_sample_file[customer_sample_file["DateTime Recorded"] < "2018-01-01"]

# Print the results
print(customers_2017_or_earlier)

# Output the records
customers_2017_or_earlier.to_excel("Customers2017.xlsx")

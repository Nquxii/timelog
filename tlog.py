#!/usr/bin/python3.10
import argparse
import pandas as pd
import datetime as dt

# A small script allowing for analyses of a user's time managment
# Create the parser
my_parser = argparse.ArgumentParser(description='Log the user\'s current use of time in a csv file')

# Add activity and description arguments
my_parser.add_argument('-a', type=str, help='Current activity')
my_parser.add_argument('-d', type=str, help='Description of action')
my_parser.add_argument('-p', type=str, help='Classification of productivity')

# Execute the parse_args() method
args = my_parser.parse_args()

# Variables needed to add to the csv
activity = args.a
description = args.d
productivity = args.p

# Time and date of the data
time = dt.datetime.now().strftime('%I:%M %p')
date = dt.datetime.today().strftime('%m-%d')

existingData = pd.read_csv('data.csv', index_col=0)

# What kind of analyses would I want to perform on my time mgmt data?
# time / effectiveness

# The new document or "log" of user time
newLog = pd.DataFrame({
    "activity": [activity],
    "description": [description],
    "time": [time],
    "date": [date],
    "productive": [productivity],
    },

    # Set the new index to +1 Append given user information to the csv file
    index = [existingData.index[-1] + 1]
)

# Append the new log of user data to the csv
newLog.to_csv('data.csv', mode='a', header=False)

print(f'{activity} at {time} added to data.csv.')

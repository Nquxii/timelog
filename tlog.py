#!/usr/bin/env python3
import argparse
import pandas as pd
import datetime as dt
import os

# A small script allowing for analyses of a user's time managment

#CSV file
logcsv = os.path.join(os.path.dirname(__file__), 'data.csv')

# Create the parser
my_parser = argparse.ArgumentParser(description='Log the user\'s current use of time in a csv file')

# Add activity and description arguments [all are optional]
my_parser.add_argument('-a', metavar="ACTIVITY", type=str, help='add an activity')
my_parser.add_argument('-d', metavar="DESC", type=str, help='description of the log')
my_parser.add_argument('-i', metavar="IS_PRODUCTIVE", type=str, help='whether or not the log is considered productive')

# Execute the parse_args() method
args = my_parser.parse_args()

# Variables needed to add to the csv
activity = args.a
description = args.d
productivity = args.i

# Time and date of the data
time = dt.datetime.now().strftime('%I:%M %p')
date = dt.datetime.today().strftime('%m-%d')

# Set a variable for our existing csv time log
existingData = pd.read_csv(logcsv)

# What kind of analyses would I want to perform on my time mgmt data?
# time / effectiveness

# The new document or "log" of user time
newLog = pd.DataFrame({
    "Date": [date],
    "Time": [time],
    "Activity": [activity],
    "Description": [description],
    "Productive": [productivity],
    },

    # Set the new index to +1 Append given user information to the csv file
    index = [existingData.index[-1] + 1]
)

# Append the new log of user data to the csv
newLog.to_csv(logcsv, mode='a', header=False)

print(f'{activity} at {time} added to {logcsv}')

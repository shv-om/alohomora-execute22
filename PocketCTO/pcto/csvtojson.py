import csv
import json

def convjson(csvFilename):
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename, encoding = 'utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)
        # Converting rows into dictionary and adding it to data

        for rows in csvRead:
            key = rows.keys()
            val = rows.values()
            mydata['value'] = list(key)[0]
            mydata['count'] = list(val)[0]

            print(mydata)

    # dumping the data
    return json.dumps(mydata)

convjson('sample1/termCountDF.csv')

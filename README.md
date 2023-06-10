# CSVHandler

CSVHandler is a Python class that uses the _pandas_ and  _numpy_ libraries to streamline data extrapolation from csv files. Its purpose is to simplify certain tasks like extracting specific columns and rows from any given csv file so that data processing for later use in any program is more straightforward while mainting fast access speeds and low computing complexity. Its core functionaliy focuses on retrieving data in order to minimize the obfuscation of csv data that could lead to errors or corrupted data.

### Requirements

This class requires that the _pandas_ and  _numpy_ libraries are installed on the environment used to run it. For fast setup, use the ```pip``` command to run the requirements.txt provided in the repo with:

````pip install -r requirements.txt````

### Installation

1. Make sure the latest version of Python is installed on your system
2. Make sure the required libraries are installed (_pandas_ and  _numpy_)
3. Download the CSVHandler.py file to any local directory

### Examples
_These examples use the AAPLhistoricaldata.csv file (which can be found in this repo). Save the file locally and change the file patch accordingly to run the following examples_

1. This code snippet gets the entire date column from the AAPLhistoricaldata.csv file based on its numerical index.

````
import CSVHandler as CSVH
csvHandler = CSVH.CSVHandler()
csvFile = 'C:\\...\\AAPLhistoricaldata.csv' # Replace with the path to the CSV file as a string
AAPLDates = csvHandler.getColumnFromCSV(csvFile, 0)
print(AAPLDates)
````


2. This code gets the last recorded date in the date column from the AAPLhistoricaldata.csv.

````
import CSVHandler as CSVH
csvHandler = CSVH.CSVHandler()
csvFile = 'C:\\...\\AAPLhistoricaldata.csv' # Replace with the path to the CSV file as a string
AAPLDates = csvHandler.getColumnFromCSV(csvFile, 0)
AAPLLastRecordedDate = csvHandler.getRowFromCSV(csvFile, AAPLDates.shape[0]-1)
print(AAPLLastRecordedDate)
````

3. This code snippet gets the date, open and close price columns from the AAPLhistoricaldata.csv file based on their numerical index range.

````
import CSVHandler as CSVH
csvHandler = CSVH.CSVHandler()
csvFile = 'C:\\...\\AAPLhistoricaldata.csv' # Replace with the path to the CSV file as a string
AAPLColumns = csvHandler.getMultipleColumnsFromCSV(csvFile, (0, 2))
print(AAPLColumns)

````

4. This code snippet gets the open price and close price values from the AAPLhistoricaldata.csv between the last recorded entry date and 3 months (90 days/data points) prior to that.

````
import CSVHandler as CSVH
csvHandler = CSVH.CSVHandler()
csvFile = 'C:\\...\\AAPLhistoricaldata.csv' # Replace with the path to the CSV file as a string
AAPLColumns = csvHandler.getMultipleColumnsFromCSV(csvFile, (0, 2))
AAPLRows = csvHandler.getMultipleRowsFromCSV(csvFile, (AAPLColumns.shape[0] - 90, AAPLColumns.shape[0]))
print(AAPLRows)

````

5. This code takes a data frame with certain data entries and exports it to a csv file at a specific file path.

````
import CSVHandler as CSVH
csvHandler = CSVH.CSVHandler()
csvFile = 'C:\\...\\AAPLhistoricaldata.csv' # Replace with the path to the CSV file as a string
AAPLColumns = csvHandler.getMultipleColumnsFromCSV(csvFile, (0, 2))
AAPLRows = csvHandler.getMultipleRowsFromCSV(csvFile, (AAPLColumns.shape[0] - 90, AAPLColumns.shape[0]))
csvHandler.exportDataFrameToCSV(AAPLSelectedRows, folder = 'AAPLData', savefileas = 'AAPLCustomData', fileextension = '.csv')
````


import csv
import array
import numpy as np
import pandas as pd
from pandas import DataFrame
import os


class CSVHandler():

    #Function that retrieves a column from a CSV given its numerical index
    #Returns the column at the numerical index in the CSV file
    def getColumnFromCSV(self, csvFilePath, columnIndex):
        
        csvDataFrame = pd.read_csv(csvFilePath)

        csvColumn = csvDataFrame.iloc[:,columnIndex]

        return csvColumn
    
    #Function that retrieves a row from a CSV given its numerical index
    #Returns the row at the numerical index in the CSV file
    def getRowFromCSV(self, csvFilePath, rowIndex):
        
        csvDataFrame = pd.read_csv(csvFilePath)
        
        csvRow = csvDataFrame.iloc[rowIndex]
        
        return csvRow
    
    #Function that retrieves multiple rows from a CSV given a desired numerical index range
    #Returns the rows at the numerical index range in the CSV file
    def getMultipleRowsFromCSV(self, csvFilePath, rowIndexRange):

        csvDataFrame = pd.read_csv(csvFilePath)
        
        csvRows = pd.DataFrame(csvDataFrame.iloc[rowIndexRange[0]:rowIndexRange[1]])

        return csvRows
    
    #Function that retrieves multiple columns from a CSV given a desired numerical index range
    #Returns the columnss at the numerical index range in the CSV file
    def getMultipleColumnsFromCSV(self, csvFilePath, columnIndexRange):
        
        csvDataFrame = pd.read_csv(csvFilePath)
        
        csvColumns = pd.DataFrame(csvDataFrame.iloc[:,columnIndexRange[0]:columnIndexRange[1]])

        return csvColumns
    
    #Function that saves a Data Frame to a CSV at a given folder path along with a desired file name to save it as
    def exportDataFrameToCSV(self, dataFrame, folder = '', savefileas = '', fileextension = '.csv'):
        savedir = ''
        if folder != '':
            savedir = os.getcwd()+'\\'+folder
        else:
            savedir = os.getcwd()+'\\'
        savefolderpath = savedir
        savefilepath = savedir +'\\'+ savefileas + fileextension
        if not os.path.exists(savefolderpath):
            os.makedirs(savefolderpath)
            dataFrame.to_csv(savefilepath, index=False)
            print('Data Frame saved to: ' + savefilepath)
        elif os.path.exists(savefolderpath):
            dataFrame.to_csv(savefilepath, index=False)
            print('Data Frame saved to: ' + savefilepath)
        else:
            print('Data Frame could not be saved to: ' + savefilepath +'Please try again.')

    #Function that imports a CSV file into a Data Frame
    #Returns the imported CSV as a Data Frame
    def importCSVToDataFrame(self, csvFilePath):
        csvDataFrame = pd.read_csv(csvFilePath)
        return csvDataFrame
